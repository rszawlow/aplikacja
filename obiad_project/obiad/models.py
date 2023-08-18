from django.db import models
from django.contrib.auth.models import User

class ObiadChoice(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wybor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

