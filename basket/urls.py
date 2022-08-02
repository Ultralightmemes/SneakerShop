from django.urls import path

from . import views

app_name = 'basket'
urlpatterns = [
    path('', views.add_sneaker, name='add_sneaker'),
    path('delete/', views.delete_sneaker, name='delete_sneaker')
]
