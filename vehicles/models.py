from django.db import models

# Create your models here.
class Van(models.Model):

    st = (
        ('W','Working'),('NW','Not working')
    )

    id = models.CharField(primary_key=True, max_length=150)
    company = models.CharField(max_length=250)
    model = models.CharField(max_length=100)
    # color = models.CharField(max_length=100, choices= c)
    speed = models.CharField(max_length=50, default='NA')
    avgSpeed = models.CharField(max_length=50, default='NA')
    enStatus = models.CharField(max_length=50, choices=st)
    flLevel = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50, default='NA')