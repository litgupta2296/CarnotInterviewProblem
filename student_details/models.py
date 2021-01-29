from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=False,blank=False)
    book_author = models.CharField(max_length=100,null=True,blank=True)
    date_of_publication = models.DateField(null=True,blank=True)
    pages = models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.title
    
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    region_id = models.IntegerField(null=False,blank=False)
    school_name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    principal = models.CharField(null=False,max_length=150,blank=False)
    phone = models.CharField(max_length=8,validators=[RegexValidator(regex='^[0-9]{3}-[0-9]{4}$',message="invalid phone number pattern")])
    address = models.CharField(max_length=150,null=False,blank=False)

    def __str__(self):
        return self.school_name


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(null=False,max_length=20,blank=False)
    last_name = models.CharField(null=True,max_length=25,blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10,null=True,blank=True)
    book_id = models.ForeignKey(Book,on_delete=models.SET_NULL,null=True,blank=True)
    school_id = models.ForeignKey(School,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)


    
