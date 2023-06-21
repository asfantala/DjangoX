from django.shortcuts import render

# Create your views here.
from django.views.generic import (
 ListView,
 DetailView,
 CreateView,
 UpdateView,
 DeleteView,
)
from django.urls import reverse_lazy
from .models import Clothing


class clothesListView(ListView):
 template_name = "clothes/clothes-list.html"
 model = Clothing


class clothesDetailView(DetailView):
 template_name = "clothes/clothes-detail.html"
 model = Clothing


class clothesCreateView(CreateView):
 template_name = "clothes/clothes-create.html"
 model = Clothing
 fields = ['name', 'purchaser', 'price', 'size', 'color', 'description']
 success_url= reverse_lazy("clothing_list")


class clothesUpdateView(UpdateView):
 template_name = "clothes/clothes-update.html"
 model = Clothing
 fields = ['name', 'purchaser', 'price', 'size', 'color', 'description']
 success_url= reverse_lazy("clothing_list")

class clothesDeleteView(DeleteView):
 template_name = "clothes/clothes-delete.html"
 model = Clothing
 success_url = reverse_lazy("clothing_list")