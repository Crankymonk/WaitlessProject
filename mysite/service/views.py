from django.db import models
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Item
from cart.forms import CartAddItemForm


def item_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    items = Item.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        items = items.filter(category=category)
        return render(request, 'service/item/list.html',
                      {'category': category,
                       'categories': categories,
                       'items': items})

    return render(request, 'service/item/list.html',
                  {'category': category,
                   'categories': categories,
                   'items': items})
'''
render(request, 'service/item/list.html',
                      {'category': category,
                       'categories': categories,
                       'items': items})
'''


def item_detail(request, slug, id):
    item = get_object_or_404(Item, slug=slug, id=id, available=True)
    cart_item_form = CartAddItemForm()
    return render(request, 'service/item/detail.html',
                  {'item': item,
                   'cart_item_form': cart_item_form})
