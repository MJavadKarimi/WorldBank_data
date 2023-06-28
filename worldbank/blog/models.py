from django.db import models

# Create your models here.

class Indicators(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=300)
    class Meta:
        db_table = 'indicators'


class Countries(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=80)
    class Meta:
        db_table = 'countries'


class Datas(models.Model):
    id = models.IntegerField(primary_key=True)
    indicator = models.ForeignKey(Indicators, on_delete=models.CASCADE, db_column='indicator')
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, db_column='country')
    date = models.CharField(max_length=20)
    amount = models.CharField(max_length=40)
    class Meta:
        db_table = 'datas'