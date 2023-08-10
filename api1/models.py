from django.db import models

class Car(models.Model):
    model= models.CharField(max_length=40)
    color = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.model
