from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Sum
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .models import Category


def paginate(objects, paginate_num, page_number):
    paginator = Paginator(objects, paginate_num)
    page_number = page_number
    return paginator.get_page(page_number)


def get_cached_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('categories', categories, 60)
    return categories


def get_sneakers_cost(sneakers):
    return sneakers.aggregate(Sum('cost'))['cost__sum']


def register_form(request, form):
    is_register = False
    if form.is_valid():
        user = form.save()
        login(request, user)
        is_register = True
    return is_register


def login_form(request, form):
    is_login = False
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        is_login = True
    return is_login


def change_password(request, form):
    is_changed = False
    if form.is_valid():
        user = request.user
        if user.check_password(request.POST['old_password']):
            if request.POST['password1'] == request.POST['password2']:
                user.set_password(request.POST['password1'])
                user.save()
                login(request, user)
                is_changed = True
    return is_changed
