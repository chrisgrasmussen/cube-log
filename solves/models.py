from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Solve(models.Model):
    solve_time = models.FloatField(null=True, blank=True, default=0.0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.solve_time)