from django.db import models

class Customers(models.Model):
    firs_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    emali = models.TextField(max_length=100)   
    phone_number = models.TextField(max_length=20)
    Address = models.TextField(max_length=200)
    City = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    postal_Code = models.TextField(max_length=20)