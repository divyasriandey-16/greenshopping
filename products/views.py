from django.shortcuts import render
from .models import Product

def search_product(request):
    query = request.GET.get('q', '')
    product = Product.objects.filter(barcode=query).first()

    return render(request, 'search.html', {'product': product})
