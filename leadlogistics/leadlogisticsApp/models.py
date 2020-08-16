from django.db import models
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django import template
from django.contrib.auth.models import User
register = template.Library()
from django.urls import reverse


DOCKET_CHOICES = (
    ("Shipment Pickup From Origin", "Shipment Pickup From Origin"),
    ("Received At Origin Warehouse", "Received At Origin Warehouse"),
    ("In Transit", "In Transit"),
    ("Received At Destination WareHouse", "Received At Destination WareHouse"),
    ("Out For Delivery", "Out For Delivery"),
    ("Delivered", "Delivered"),
)

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.

class Docket(models.Model):
    DocketId = models.CharField(max_length=50, unique=True, validators=[alphanumeric])
    DocketStatus  = models.CharField(max_length=128,choices = DOCKET_CHOICES)
    EntryText = models.CharField(max_length=128,blank=True,default='')

    #slug = models.SlugField(allow_unicode=True,unique=True)
    #DocketStatus  = models.CharField(max_length=128)
    #slug = models.SlugField(allow_unicode=True,unique=True)

    def __str__(self):
        return self.DocketId
    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.DocketId)
    #     super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("leadlogisticsApp:nodata")

    class Meta:
        unique_together = ('DocketId','DocketStatus')

        #self.slug = slugify(self.name)
        #print("pk is : ",self.pk)
        #return reverse("leadlogisticsApp:detail",kwargs={'pk':self.kwargs.get("id")})


class Contact(models.Model):
    name = models.CharField(max_length=128,blank=False)
    email = models.EmailField(blank=False)
    phone = models.PositiveIntegerField(blank=False)
    subject = models.CharField(max_length=256,blank=False)
    requirements = models.TextField()


    def __str__(self):
        return self.name
