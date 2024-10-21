from django.db import models

# Create your models here.
class aboutap(models.Model):
    apabout=models.TextField()
    aboutMinister=models.TextField()
class aboutimages(models.Model):
    image=models.ImageField(upload_to='images/')
class place1(models.Model):
    placename=models.CharField(max_length=50)
    history=models.TextField()
class place1images(models.Model):
    img1=models.ImageField(upload_to='images/')
class place1video(models.Model):
    video=models.FileField(upload_to='video/')
    vdate=models.DateField()
class place2(models.Model):
    placename=models.CharField(max_length=50)
    history=models.TextField()
class place2images(models.Model):
    img1=models.ImageField(upload_to='images/')
class place2video(models.Model):
    video=models.FileField(upload_to='video/')
    vdate=models.DateField()
