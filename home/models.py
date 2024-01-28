from django.db import models

# Create your models here.
class name(models.Model):
    username = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 200)
    def __str__(self):
        return self.username