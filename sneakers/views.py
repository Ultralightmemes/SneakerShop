from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, UserLoginForm, UpdateUserForm
from .models import Sneaker, Category
from basket.models import Order
from .service import *


class IndexView(generic.ListView):
    context_object_name = 'latest_sneakers_list'
    template_name = 'sneakers/index.html'

    def get_queryset(self):
        return Sneaker.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class SneakerDetailView(generic.DetailView):
    model = Sneaker
    template_name = 'sneakers/sneaker.html'


class SneakerView(generic.ListView):
    paginate_by = 2
    template_name = 'sneakers/sneaker_list.html'
    model = Sneaker

    def get(self, request, *args, **kwargs):
        page_obj = paginate(Sneaker.objects.all(), 5, request.GET.get('page'))
        categories = get_cached_categories()
        return render(request, 'sneakers/sneaker_list.html',
                      {'page_obj': page_obj,
                       'categories': categories,
                       'sneakers_count': Sneaker.objects.all().__len__(),
                       })


def get_category(request, pk):
    page_obj = paginate(Sneaker.objects.filter(category_id=pk), 5, request.GET.get('page'))
    return render(request, 'sneakers/sneaker_list.html',
                  {'page_obj': page_obj,
                   'categories': Category.objects.all(),
                   'category': Category.objects.get(pk=pk),
                   'sneakers_count': Sneaker.objects.all().__len__(),
                   })


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if register_form(request, form):
            messages.success(request, 'Вы успешно зарегистрировались!')
            redirect('sneakers:index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'sneakers/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('sneakers:profile')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if login_form(request, form):
            return redirect('sneakers:index')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'sneakers/login.html', {'form': form})


@login_required(login_url=reverse_lazy('sneakers:login'))
def get_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST)
        if change_password(request, form):
            return redirect('sneakers:profile')
        else:
            messages.error(request, 'Ошибка смены пароля')
    else:
        form = UpdateUserForm()
    return render(request, 'sneakers/profile.html', {'form': form, 'side': 'profile'})


def exit_profile(request):
    logout(request)
    return redirect('sneakers:login')


@login_required(login_url=reverse_lazy('sneakers:login'))
def get_basket(request):
    sneakers = Sneaker.objects.filter(order__basket__user_id=request.user.id, order__is_active=True)
    orders = Order.objects.filter(basket__user=request.user.id, is_active=True)
    return render(request, 'sneakers/basket.html', {'orders': orders, 'sneakers_cost': get_sneakers_cost(sneakers)})


@login_required(login_url=reverse_lazy('sneakers:login'))
def get_history(request):
    sneakers = Sneaker.objects.filter(order__basket__user_id=request.user.id)
    orders = Order.objects.filter(basket__user=request.user.id).select_related('sneaker', 'size')
    return render(request, 'sneakers/history.html', {'orders': orders, 'sneakers_cost': get_sneakers_cost(sneakers),
                                                     'side': 'history'})
