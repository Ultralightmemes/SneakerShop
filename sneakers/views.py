from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserLoginForm, UpdateUserForm
from .models import Sneaker, Category


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
        paginator = Paginator(Sneaker.objects.all(), 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        categories = Category.objects.all()
        return render(request, 'sneakers/sneaker_list.html',
                      {'page_obj': page_obj,
                       'categories': categories
                       })


def get_category(request, pk):
    sneakers = Sneaker.objects.filter(category_id=pk)
    paginator = Paginator(sneakers, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    return render(request, 'sneakers/sneaker_list.html',
                  {'page_obj': page_obj,
                   'categories': categories,
                   'category': category,
                   })


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect('sneakers:index')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'sneakers/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('sneakers:index')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'sneakers/login.html', {'form': form})


def get_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(data=request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(request.POST['old_password']):
                if request.POST['password1'] == request.POST['password2']:
                    user.set_password(request.POST['password1'])
                    user.save()
                login(request, user)
                return redirect('sneakers:profile')
        else:
            messages.error(request, 'Ошибка смены пароля')
    else:
        form = UpdateUserForm()
    return render(request, 'sneakers/profile.html', {'form': form})
