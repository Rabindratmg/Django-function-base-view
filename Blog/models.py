from django.db import models

# Create your models here.



class Blog(models.Model):
    title=models.CharField(max_length=200,blank=False)
    description=models.TextField(max_length=500,blank=False)


    def __str__(self):
        return self.title
