from django.shortcuts import render
from store.models import Product, ReviewRating
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import Avg

def home(request):
    reviews = None
    products = Product.objects.filter(is_available=True).annotate(avg_rating=Avg('reviewrating__rating')).order_by('-avg_rating', '-created_date')
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    context = {'products': products,
               'reviews': reviews}
    return render(request, 'home.html', context)

def about(request):
    team_members = [
        {'name': 'Harsh Moradiya', 'image': '/static/images/team/team-1.jpg'},
        {'name': 'Ankur Mangroliya', 'image': '/static/images/team/team-2.jpg'},
        {'name': 'Mohil Jivani', 'image': '/static/images/team/team-3.jpg'},
        {'name': 'Smit Maniya', 'image': '/static/images/team/team-4.jpg'}
    ]
    return render(request, 'about.html', {'team_members': team_members})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            f'Message from {name}',  
            message,  
            email,  
            ['your_email@example.com'], 
        )
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'contact.html')
