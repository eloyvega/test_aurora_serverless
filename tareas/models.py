from django.db import models

# Create your models here.
class Tarea(models.Model):
    tarea_text = models.CharField(max_length=200)