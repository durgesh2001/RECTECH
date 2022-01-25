from django.db import models
#models for user
class USER(models.Model):
     Firstname = models.CharField(max_length=50)
     Lastname = models.CharField(max_length=50)
    
     Address = models.CharField(max_length=50)
     contact = models.BigIntegerField()
     Email = models.EmailField(max_length=50)
     Password = models.CharField(max_length=16)




