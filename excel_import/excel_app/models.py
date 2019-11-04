from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email_id=models.EmailField(max_length=100,null=True,blank=True)
    phone_number=models.BigIntegerField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
