import threading
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

class ActiveUserMiddleware(MiddlewareMixin):
    active_users = set()
    total_active_users = set()
    lock = threading.Lock()

    def process_request(self, request):
        user = request.user
        if user.is_authenticated:
            with self.lock:
                self.active_users.add(user.id)
                self.total_active_users.add(user.id)

    def process_response(self, request, response):
        return response

    @classmethod
    def get_active_user_count(cls):
        with cls.lock:
            return len(cls.active_users)

    @classmethod
    def get_total_active_user_count(cls):
        with cls.lock:
            return len(cls.total_active_users)

    @classmethod
    def remove_active_user(cls, user_id):
        with cls.lock:
            cls.active_users.discard(user_id)

# Signal receiver for user logout
@receiver(user_logged_out)
def user_logged_out_handler(sender, request, user, **kwargs):
    ActiveUserMiddleware.remove_active_user(user.id)