from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import (
    clothesListView,
    clothesDetailView,
    clothesCreateView,
    clothesUpdateView,
    clothesDeleteView,
)


class TestUrls(SimpleTestCase):
    def test_clothing_list_url(self):
        url = reverse('clothing_list')
        self.assertEqual(resolve(url).func.view_class, clothesListView)

    def test_clothing_detail_url(self):
        url = reverse('clothing_detail', args=[1])  # Assuming the PK is 1
        self.assertEqual(resolve(url).func.view_class, clothesDetailView)

    def test_clothing_create_url(self):
        url = reverse('clothing_create')
        self.assertEqual(resolve(url).func.view_class, clothesCreateView)

    def test_clothing_update_url(self):
        url = reverse('clothing_update', args=[1])  # Assuming the PK is 1
        self.assertEqual(resolve(url).func.view_class, clothesUpdateView)

    def test_clothing_delete_url(self):
        url = reverse('clothing_delete', args=[1])  # Assuming the PK is 1
        self.assertEqual(resolve(url).func.view_class, clothesDeleteView)
