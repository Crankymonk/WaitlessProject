from django.shortcuts import render
from .models import OrderItem, CallItem, Staff
from .forms import OrderCreateForm, CallCreateForm
from cart.cart import Cart
# Create your views here.

def check_shisha_master(request):
    '''Call shisha master to selected table'''

    workers = Staff.objects.all()
    for guy in workers:
        worker = guy.name
    call = CallItem(request)
    if request.method == 'POST':
        form = CallCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            CallItem.objects.create(order=order,
                                     worker='worker')

            return render(request,
                          'orders/shishamaster.html',
                          {'worker': worker})
    else:
        form = CallCreateForm()
    return render(request,
                  'orders/shishamaster_check.html',
                  {'worker': worker, 'form': form})




def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['item'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})


