from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

#signals = pre_save, post_save, pre_delete, post_delete


@receiver(pre_save, sender=Car)
def call_car_api(sender, instance, **kwargs):
    print("Car API called")
    print(sender,instance,kwargs)