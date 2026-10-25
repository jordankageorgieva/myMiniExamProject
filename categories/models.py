from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    profile = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="categories",
    )

    def __str__(self):
        return self.name
