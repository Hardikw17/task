from django.db import models

# Create your models here.

class Movie(models.Model):
    # mid =models.IntegerField(   )
    mtitle = models.CharField(max_length=50)
    mrating = models.IntegerField()
    mrelease = models.TextField()
    mid = models.IntegerField()
    mgeneres = models.CharField(max_length=100)

    def __str__(self):
        return self.mtitle
