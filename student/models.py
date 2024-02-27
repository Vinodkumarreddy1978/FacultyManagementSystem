from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class faculty(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media')
    Subject=models.CharField(max_length=49)
    Experience=models.IntegerField()
    Age=models.IntegerField()
    Qualification=models.CharField(max_length=48)
    # Achievements=models.CharField(max_length=40)
    Email=models.EmailField(max_length=40)
    Mobile_Number=models.IntegerField()
    def __str__(self):
        return self.name
