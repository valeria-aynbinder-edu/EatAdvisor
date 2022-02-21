from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    country = models.CharField(null=False, blank=False, max_length=128)
    city = models.CharField(null=False, blank=False, max_length=128)
    address = models.CharField(null=True, blank=True, max_length=128)
    type = models.CharField(null=True, blank=True, max_length=128)
    price_range = models.PositiveSmallIntegerField(
        null=False, blank=False, default=2, validators=[MinValueValidator(1), MaxValueValidator(3)])
    pic_url = models.URLField(null=True, blank=True)
    reviewers = models.ManyToManyField(to=User, through='Review')

    class Meta:
        db_table = "restaurants"


class Review(models.Model):

    TRAVELER_TYPE_CHOICES = [
        ('FAMILIES', 'families'),
        ('COUPLES', 'Couples'),
        ('SOLO', 'Solo'),
        ('BUSINESS', 'Business'),
        ('FRIENDS', 'Friends'),
    ]
    restaurant = models.ForeignKey(Restaurant, on_delete=models.RESTRICT, null=False, blank=False, )
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=False, blank=False)
    traveler_type = models.CharField(null=True, blank=True, choices=TRAVELER_TYPE_CHOICES, max_length=64)
    stars = models.PositiveSmallIntegerField(null=False, blank=False,
                                             validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(null=False, blank=False, max_length=256)
    text = models.TextField(null=False, blank=False)
    date = models.DateField(null=False, blank=False)

    class Meta:
        db_table = "reviews"



