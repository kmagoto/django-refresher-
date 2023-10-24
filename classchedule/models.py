from django.db import models
from datetime import time

# Create your models here.

class PersonalData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom_number = models.IntegerField(default=(2))

    #@property
    def __str__(self):
        return f"{self.name}: classroom{self.classroom_number}on age{self.age}"

class ClassSchedule(models.Model):
    topic = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=(2))
    classroom = models.ForeignKey(PersonalData,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.topic} at {self.start_time} on {self.date}"



