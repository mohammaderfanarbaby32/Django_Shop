from django.shortcuts import render
from .models import Customers
from django.http import HttpResponse, JsonResponse
# Show all field---------------------------------------------
def W(request):
    words = Customers.objects.all()
    word_list = []
    for word in words:
        word_dict = {'name': word.name, 'age': word.age}
        word_list.append(word_dict)
    return JsonResponse(word_list, safe=False)
#------------------------------------------------------------



# Customers Edit--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def serch_field_Customer(request, first_name):
    try:
        word = Customers.objects.get(first_name=first_name)
        word_dict = {'first_name': word.first_name, 'Last_name': word.last_name,'email':word.email,'phone number': word.phone_number, 'Address': word.Address,'City':word.City, 'State': word.state,'postal_Code':word.postal_Code }
        return JsonResponse(word_dict)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)

def add_field_Customer(request,first_name,last_name,email,phone_number,Address,City,state,postal_Code):
    new_word = Customers(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,Address=Address,City=City,state=state,postal_Code=postal_Code)
    new_word.save()
    return HttpResponse('Word added successfully!')

def delete_field_Customer(request, first_name):
    Delete_field = Customers.objects.get(first_name=first_name)
    Delete_field.delete()
    return HttpResponse('Word deleted successfully!')

def Update_field_Customer(request,first_name,last_name,email,phone_number,Address,City,state,postal_Code):
  a=Customers.objects.get(first_name=first_name)
  a.first_name=first_name
  a.last_name=last_name
  a.email=email
  a.phone_number=phone_number
  a.Address=Address
  a.City=City
  a.state=state
  a.postal_Code=postal_Code
  a.save()
  return HttpResponse('Word Update successfully!')
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Products Edit-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def serch_field_Products(request, Product_name):
    try:
        word = Customers.objects.get(Product_name=Product_name)
        word_dict = {'Product_name': word.Product_name, 'description': word.last_name,'email':word.email,'phone number': word.phone_number, 'Address': word.Address,'City':word.City, 'State': word.state,'postal_Code':word.postal_Code }
        return JsonResponse(word_dict)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)

def add_field_Products(request,first_name,last_name,email,phone_number,Address,City,state,postal_Code):
    new_word = Customers(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,Address=Address,City=City,state=state,postal_Code=postal_Code)
    new_word.save()
    return HttpResponse('Word added successfully!')

def delete_field_Products(request, first_name):
    Delete_field = Customers.objects.get(first_name=first_name)
    Delete_field.delete()
    return HttpResponse('Word deleted successfully!')

def Update_field_Products(request,first_name,last_name,email,phone_number,Address,City,state,postal_Code):
  a=Customers.objects.get(first_name=first_name)
  a.first_name=first_name
  a.last_name=last_name
  a.email=email
  a.phone_number=phone_number
  a.Address=Address
  a.City=City
  a.state=state
  a.postal_Code=postal_Code
  a.save()
  return HttpResponse('Word Update successfully!')