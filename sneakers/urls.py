from django.urls import path

from . import views

app_name = 'sneakers'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SneakerDetailView.as_view(), name='sneaker')
]
