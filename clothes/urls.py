from django.urls import path
from .views import clothesListView, clothesDetailView, clothesCreateView, clothesUpdateView, clothesDeleteView

urlpatterns = [
    path('clothes/', clothesListView.as_view(), name='clothing_list'),
    path('clothes/<int:pk>/', clothesDetailView.as_view(), name='clothing_detail'),
    path('clothes/create/', clothesCreateView.as_view(), name='clothing_create'),
    path('clothes/<int:pk>/update/',
         clothesUpdateView.as_view(), name='clothing_update'),
    path('clothes/<int:pk>/delete/',
         clothesDeleteView.as_view(), name='clothing_delete'),
]
