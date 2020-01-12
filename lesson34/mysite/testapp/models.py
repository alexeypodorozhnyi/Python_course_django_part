from django.db import models
from datetime import datetime, timedelta


# Create your models here.


class Animal(models.Model):
    ANIMAL_CHOISES = [
        ('1', 'Bajor'),
        ('2', 'Monkey'),
        ('3', 'Bear')
    ]
    GENDER_CHOISES = [
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other')
    ]
    type = models.CharField(max_length=50, choices=ANIMAL_CHOISES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOISES)
    age = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    date_arrived = models.DateTimeField(auto_now_add=True)


class Visitor(models.Model):
    GENDER_CHOISES = [
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other')
    ]
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOISES, max_length=20)
    age = models.PositiveIntegerField()


class Ticket(models.Model):
    date_buy = models.DateTimeField(auto_now_add=True)
    date_duration = models.DateTimeField(default=datetime.today() + timedelta(days=1))
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)


class Visit(models.Model):
    user = models.ForeignKey(Visitor, on_delete=models.DO_NOTHING)
    animal = models.ForeignKey(Animal, on_delete=models.DO_NOTHING)
    date_time_visit = models.DateTimeField(auto_now_add=True)
