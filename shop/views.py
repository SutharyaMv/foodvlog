from django.shortcuts import render,get_object_or_404
from . models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
# Create your views here.


def home(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = products.objects.filter(category=c_page, available=True)
    else:
        prodt = products.objects.filter(available=True)
        paginator = Paginator(prodt, 3)  # Show 3 products per page

        page = request.GET.get('page', 1)
        try:
            prodt = paginator.page(page)
        except EmptyPage:
            prodt = paginator.page(paginator.num_pages)

    cat = categ.objects.all()
    return render(request, 'home.html', {'pr': prodt, 'ct': cat})

def prodDetails(request,c_slug,product_slug):
    try:
        prod=products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'item.html',{'pr':prod})



def searching(request):
    prod=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        prod=products.objects.all().filter(Q (name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})

def menu_details(request):
    # Fetch products to display in the menu
    prodt = products.objects.filter(available=True)  # Or any other condition
    return render(request, 'menu.html', {'pr': prodt})



def about(request):
    return render(request, 'about.html')