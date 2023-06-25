from django.db import models

# Create your models here.

class Indicators(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=300)


class Countries(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=80)


class Datas(models.Model):
    id = models.constants
    indicator_id = models.ForeignKey(Indicators, on_delete=models.CASCADE)
    country_id = models.ForeignKey(Countries, on_delete=models.CASCADE)
    date = models.CharField(max_length=20)
    amount = models.CharField(max_length=40)