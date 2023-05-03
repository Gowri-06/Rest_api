from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return self.title
    
class Interest(models.Model):
    interests = models.CharField(max_length=200)
    def __str__(self):
        return self.interests

class City(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city


    
class Person(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.IntegerField(max_length=10,null=False)
    interest = models.ManyToManyField(Interest)

    def __str__(self):
        return self.name

class PersonAddress(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)

    def __str__(self):
        return self.person.name + "(" + self.street_address + ")"


