from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    TYPES = {
        (1, "Fundacja"),
        (2, "Organizacja pozarządowa"),
        (3, "Zbiórka lokalna")
    }
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models. ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=64)
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=12)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __int__(self):
        return self.quantity


