from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item

class ItemAPITests(APITestCase):
    def setUp(self):
        self.item_data = {
            "item_name": "Excalibur",
            "item_type": "Weapon",
            "rarity": "Legendary",
            "stat_value": 150,
            "is_equipped": False
        }
        self.item = Item.objects.create(**self.item_data)
        self.list_url = reverse('item-list')
        self.detail_url = reverse('item-detail', kwargs={'pk': self.item.id})

    def test_create_item(self):
        data = {
            "item_name": "Aegis Shield",
            "item_type": "Armor",
            "rarity": "Epic",
            "stat_value": 85,
            "is_equipped": True
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['item_name'], "Aegis Shield")
        self.assertEqual(response.data['stat_value'], 85)
        self.assertEqual(response.data['is_equipped'], True)

    def test_get_all_items(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_single_item(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item_name'], self.item.item_name)

    def test_update_item(self):
        updated_data = {
            "item_name": "Excalibur Reforged",
            "item_type": "Weapon",
            "rarity": "Legendary",
            "stat_value": 200,
            "is_equipped": True
        }
        response = self.client.put(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item_name'], "Excalibur Reforged")
        self.assertEqual(response.data['stat_value'], 200)
        self.assertEqual(response.data['is_equipped'], True)

    def test_delete_item(self):
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)
