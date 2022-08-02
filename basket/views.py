from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Basket, Order
from sneakers.models import Sneaker, Size


def add_sneaker(request):
    if 'size' in request.POST:
        basket, created = Basket.objects.get_or_create(user=request.user)
        Order.objects.create(basket=basket,
                             sneaker_id=request.POST['sneaker_id'],
                             size_id=request.POST['size'])
        size = Sneaker.objects.get(pk=request.POST['sneaker_id']).size_set.get(pk=request.POST['size'])
        size.count -= 1
        size.save()
    else:
        messages.error(request, 'Выберите размер')
    return redirect('sneakers:sneaker', pk=request.POST['sneaker_id'])


def delete_sneaker(request):
    order = Order.objects.get(pk=request.POST['order'])
    order.size.count += 1
    order.size.save()
    order.delete()
    return redirect('sneakers:basket')

