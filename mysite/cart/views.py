from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from service.models import Item
from .cart import Cart
from .forms import CartAddItemForm


# Create your views here.
@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for piece in cart:
        piece['update_quantity_form'] = CartAddItemForm(
                              initial={'quantity': piece['quantity'],
                                       'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
