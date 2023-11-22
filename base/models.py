from django.db import models

class Members(models.Model):
    Status = (
        ('dev','dev'),
        ('cpd','cpd'),
        ('cbd','cbd')
    )
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    division=models.CharField(max_length=200,null=True,choices=Status)
    phonenumber=models.CharField(max_length=200)
    def __str__(self):
        return self.firstname
class PostNews(models.Model):
    #image=
    title = models.CharField(max_length=200)
    texttopost=models.CharField(max_length=5000)    
    
    def __str__(self):
        return self.title
    
    
class Applicant(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    id_number=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200)
    def __str__(self):
        return self.firstname
    
    
    
    
    

