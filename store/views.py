from .models import Product



def store(request, category_slug=None):
    categories = None
    products = None