from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(User):
    level=models.SmallIntegerField(default=1)
    coincidences=models.SmallIntegerField(default=2)
    token=models.CharField(default='img',max_length=3)
    victory_text=models.CharField(default="Ganaste!",max_length=100)
    defeat_text=models.CharField(default="Perdiste!",max_length=100)
    



