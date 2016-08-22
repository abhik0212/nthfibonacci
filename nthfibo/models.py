from django.db import models
# Create your models here.

class Nthfibonacci(models.Model):
    n = models.IntegerField()
    result = models.IntegerField()
    time = models.DateTimeField()
    def _init_(self, n):
        self.n = n
