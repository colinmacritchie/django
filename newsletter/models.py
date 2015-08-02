from django.db import models

# Create your models here.

#General Form data Input class model.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self): #Python 3.3 is __str__
        return self.email


class ApplicationNew(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    email = model.EmailField()
    description = models.CharField(max_length=1000, blank=True, null=False)
    description2 = models.CharField(max_length=600, blank=True, null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    address = models.CharField(max_length=50, blank=True, null=False)
    zipcode = models.CharField(max_length=5, blank=True, null=False)
    state = models.CharField(max_length=10, blank=True, null=False)
    city = models.CharField(max_length=50, blank=True, null=False)
    country = models.CharField(max_length=50, blank=True, null=False)
    
    def __unicode__(self): #Python 3.3 is __str__
        return self.full_name
