from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls
from orders import urls as orders_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls)),
    path('', views.home, name='home'),
    path('orders/', include(orders_urls))
]
