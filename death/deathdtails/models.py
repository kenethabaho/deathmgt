from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField
from django_countries.fields import CountryField
# Create your models here.
class burial(models.Model):
    place=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    county=models.CharField(max_length=100)
    subcounty=models.CharField(max_length=100)
    parish=models.CharField(max_length=100)
    village=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)

    def __str__(self):
        return self.district

class Deceased(models.Model):
    image=models.ImageField(upload_to=None,height_field=None,width_field=None,max_length=None,null=True,blank=True)
    surname=models.CharField(max_length=100)
    givenname=models.CharField(max_length=100)
    regdate=models.DateField()
    placeofbirth=models.CharField(max_length=100,null=True,blank=True)
    dateofdeath=models.DateField()
    nameofhospital=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    municipality=models.CharField(max_length=100,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    gen=[
        ('male','male'),
        ('female','female')
    ]
    gender=models.CharField(max_length=100,choices=gen)
    occupation=models.CharField(max_length=100,null=True,blank=True)
    residence=models.CharField(max_length=100,null=True,blank=True)
    village=models.CharField(max_length=100,null=True,blank=True)
    parish=models.CharField(max_length=100,null=True,blank=True)
    subcounty=models.CharField(max_length=100,null=True,blank=True)
    district=models.CharField(max_length=100,null=True,blank=True)
    nationality=CountryField()
    NIN=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self) :
        return self.NIN
    
    

