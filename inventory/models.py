from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=100) # e.g., Weapon, Consumable, Armor
    rarity = models.CharField(max_length=100)    # e.g., Common, Epic, Legendary
    stat_value = models.IntegerField()            # e.g., damage, defense, healing amount
    is_equipped = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_name} ({self.rarity} {self.item_type})"
