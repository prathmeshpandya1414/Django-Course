from django.db import models

# Create your models here.
class student(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(max_length=200,null=True, blank=True)
    # image = models.ImageField()
    # field = models.FileField()

class Car(models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name