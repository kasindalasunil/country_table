from django.db import models

# Create your models here.

class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100,unique=True)
    language=models.CharField(max_length=100)
    def __str__(self):
        return self.country_name

class Capitals(models.Model):
    capital_id=models.IntegerField(primary_key=True)
    capitals_name=models.CharField(max_length=100,unique=True)
    country_id=models.OneToOneField(Country,on_delete=models.CASCADE)
    def __str__(self):
        return self.capitals_name
    

