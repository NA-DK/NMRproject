from django.db import models

# Create your models here.

class Formula(models.Model):
    formula = models.CharField(max_length=200)
    cid = models.IntegerField()
    structure_imageurl = models.TextField()
    hnmr_imageurl = models.TextField()
    cnmr_imageurl = models.TextField()
    
    def __str__(self):
        return self.formula

class Name(models.Model):
    name = models.CharField(max_length=200)
    cid = models.IntegerField()
    structure_imageurl = models.TextField()
    hnmr_imageurl = models.TextField()
    cnmr_imageurl = models.TextField()
    
    def __str__(self):
        return self.name