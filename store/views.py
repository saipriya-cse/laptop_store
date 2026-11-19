from django.shortcuts import render
from .models import Laptop

def home(request):
    laptops = Laptop.objects.all().order_by('-id')

    return render(request, 'store/home.html', {
        'laptops': laptops
    })