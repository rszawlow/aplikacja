from django.db import models
from django.contrib.auth.models import User

class MealChoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    want_obiad = models.BooleanField(default=False)
    want_sniadanie = models.BooleanField(default=False)
    want_kolacja = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    last_choice_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"
