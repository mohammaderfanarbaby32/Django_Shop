from django.db import models

#Customers ---------------------------------------------------------------------
class Customers(models.Model):
    Customer_id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    email = models.TextField(max_length=100)   
    phone_number = models.TextField(max_length=20)
    Address = models.TextField(max_length=200)
    City = models.TextField(max_length=50)
    state = models.TextField(max_length=50)
    postal_Code = models.TextField(max_length=20)
    

#------------------------------------------------------------------------------
#Categories-----------------------------------------------------------------
class Categories(models.Model):
    category_id = models.AutoField(primary_key=True)    
    category_name = models.TextField(max_length=50)
    category_description = models.TextField(max_length=50)
    category_image = models.TextField(max_length=50)
#Products field----------------------------------------------------------------
class Products(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)   
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.TextField(max_length=200)
    category_id = models.ForeignKey(Categories,on_delete=models.CASCADE)

#------------------------------------------------------------------------------
#Orders field-------------------------------------------------------------------
class Orders(models.Model):
    Order_id = models.AutoField(primary_key=True)    
    Customer_id = models.ForeignKey(Customers,on_delete=models.CASCADE)
    Order_date = models.TextField(max_length=50)
    total_amount = models.TextField(max_length=50)   
    payment_type = models.DecimalField(decimal_places=2, max_digits=10)
    state = models.TextField(max_length=200)

#-------------------------------------------------------------------------------
#Order_details field----------------------------------------------------------
class Order_details(models.Model):
    Order_id = models.ForeignKey(Orders,on_delete=models.CASCADE)    
    Product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    Order_name = models.TextField(max_length=50)
    quantity = models.TextField(max_length=50)   
    item_notes = models.DecimalField(decimal_places=2, max_digits=10)
    item_price = models.DecimalField(decimal_places=2, max_digits=10)
    item_discount = models.TextField(max_length=50)
    item_total = models.TextField(max_length=50)
    item_status = models.TextField(max_length=50)

#-------------------------------------------------------------------------------
#ADMIN----------------------------------------------------------------------------
class admin(models.Model):
    Usname = models.TextField(max_length=50)
    Lastname = models.TextField(max_length=50)
    age = models.TextField(max_length=50)
    password = models.TextField(max_length=20)
# python manage.py migrate