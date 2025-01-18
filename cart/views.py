

from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *  # Import your product model
from . models import *
from django.core.exceptions import ObjectDoesNotExist


def cart_details(request,ct_items=[],tot=0,count=0,cart_items=None):
    # Fetch products to display in the menu
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count+=i.quan
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci':ct_items,'t':tot,'cn':count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id
def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)  # Get the product

    # Retrieve or create the cart
    cart_id = c_id(request)
    try:
        ct = cartlist.objects.get(cart_id=cart_id)
    except cartlist.DoesNotExist:
        # If no cart is found, create a new one
        ct = cartlist.objects.create(cart_id=cart_id)
        ct.save()

    try:
        c_items = items.objects.get(prodt=prod, cart=ct)  # Check if the item is already in the cart
        if c_items.quan < c_items.prodt.stock:  # Ensure stock is not exceeded
            c_items.quan += 1
        c_items.save()
    except items.DoesNotExist:
        # If the item does not exist in the cart, create it with quantity 1
        c_items = items.objects.create(prodt=prod, quan=1, cart=ct)
        c_items.save()

    # Redirect to the cart details page after adding the item
    return redirect('cartDetails')
def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')
def cart_delete(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(products,id=product_id)
    c_items=items.objects.get(prodt=prod,cart=ct)
    c_items.delete()
    return redirect('cartDetails')
 