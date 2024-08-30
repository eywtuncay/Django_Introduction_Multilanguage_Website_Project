from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Solutions(models.Model):
    solutions_name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="solutions")
    homepage = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.solutions_name}"

