from django.db import models

# Create your models here.
class ProfileFace(models.Model):
    picture1=models.ImageField(upload_to='images/')
    picture2=models.ImageField(upload_to='images/')

class textdetaction(models.Model):
    picture1=models.ImageField(upload_to='images/')
class ppe(models.Model):
    picture1=models.ImageField(upload_to='images/')