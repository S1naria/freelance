from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Laptops
from django.shortcuts import render, get_object_or_404

def index(request):
    laptops_list = Laptops.objects.all()

    items_per_page = 1
    
    paginator = Paginator(laptops_list, items_per_page)
    
    page = request.GET.get('page')  
    laptops = paginator.get_page(page)
    
    return render(request, 'main/index.html', {'laptops': laptops})

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptops, pk=laptop_id)
    return render(request, 'main/laptop_detail.html', {'laptop': laptop})