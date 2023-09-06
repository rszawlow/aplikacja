from django.db import models
from django.contrib.auth.models import User

class MealChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(unique=True,default=None)
    sniadanie = models.BooleanField(default=False)
    obiad = models.BooleanField(default=False)
    kolacja = models.BooleanField(default=False)

    def __str__(self):
        return f"Posiłek {self.data} dla {self.user}"