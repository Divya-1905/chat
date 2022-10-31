from distutils import core
from django.db import models
class messagemodel(models.Model):
    message = models.TextField(max_length=100000)