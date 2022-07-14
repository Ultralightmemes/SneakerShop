from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Sneaker


class IndexView(generic.ListView):
    context_object_name = 'latest_sneakers_list'
    template_name = 'sneakers/index.html'

    def get_queryset(self):
        return Sneaker.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class SneakerDetailView(generic.DetailView):
    model = Sneaker
    template_name = 'sneakers/sneaker.html'
