from django.urls import path

from . import views

app_name = 'sneakers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SneakerDetailView.as_view(), name='sneaker'),
    path('sneakers/', views.SneakerView.as_view(), name='sneakers'),
    path('sneakers/category/<int:pk>/', views.get_category, name='category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.get_profile, name='profile'),
]
