from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    """Get more information about the just signed one"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    home_planet = models.CharField(max_length=90)
    height = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    mass = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(200.0)])

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.user.first_name
# Create your models here.
