from django.db import models
from django.forms import DateTimeField


# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    ID_kart=models.IntegerField()
    tugulgan_kun=models.DateField()
    create_at=models.DateTimeField(auto_now_add=True)
    desc=models.TextField()
    def __str__(self):
        return f"ismi:{self.name} familya:{self.lastname}"

