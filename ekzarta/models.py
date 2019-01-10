from django.db import models

class Employee(models.Model):
    """Blog model"""
    first_name = models.TextField(max_length=100, null=False)
    last_name = models.TextField(null=False)
    img = models.ImageField(upload_to='images/employee')
    website = models.URLField(null=True)
    email = models.EmailField()
    info = models.TextField(null=True)
    skills = models.TextField(null=True,max_length=500)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Contacts(models.Model):
    """Blog model"""
    phone_1 = models.TextField(max_length=13, null=True)
    phone_2 = models.TextField(max_length=13, null=True)
    phone_3 = models.TextField(max_length=13, null=True)
    address = models.TextField(max_length=100, null=True)
    city = models.TextField(max_length=20, null=True)

    def __str__(self):
        return self.city + ' ' + self.address

class Reviews(models.Model):
    """Reviews model"""
    v_name = models.TextField(max_length=100, null=False)
    v_review = models.TextField(max_length=300, null=False)

    def __str__(self):
        return self.v_name