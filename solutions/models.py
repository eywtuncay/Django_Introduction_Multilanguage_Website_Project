from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=200)

class Solutions(models.Model):
    solutions_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=100)
    homepage = models.BooleanField(default=False)
