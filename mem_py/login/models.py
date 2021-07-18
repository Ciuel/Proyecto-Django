from django.db import models

# Create your models here.

class Config(models.Model):
    color=models.CharField(max_length=10)
    level=models.SmallIntegerField()
    token=models.CharField(max_length=3)

    def __str__(self):
        return f'Color: {self.color}, nivel: {self.level}, token: {self.token} '

class User(models.Model):
    nick=models.CharField(max_length=25,unique=True)
    password=models.CharField(max_length=16)
    age=models.PositiveSmallIntegerField(blank=True)
    config=models.OneToOneField(Config,on_delete=models.CASCADE)

    def __str__(self):
        return self.nick