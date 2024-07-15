from django.db import models
from django.contrib.auth.models import User



class DailyCost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    descriptions = models.TextField()
    amount = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username