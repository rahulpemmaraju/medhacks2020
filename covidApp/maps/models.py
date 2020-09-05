from django.db import models

class County(models.Model):
    name=models.CharField(max_length=30) #name of county
    population=models.IntegerField(default=0) #population of county
    current_cases=models.IntegerField(default=0) #current cases
    predicted_cases=models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
