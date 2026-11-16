from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="categories",
    )

    # profile = models.ForeignKey(
    #     to='profiles.Profile',
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    #     related_name="categories",
    # )

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)

    category = models.ForeignKey(
        to='categories.Category',
        on_delete=models.CASCADE,
        related_name="subcategories",
    )

    def __str__(self):
        return self.name
