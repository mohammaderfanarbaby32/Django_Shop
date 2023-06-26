from django.shortcuts import render
from .models import Customers, Products,Categories,Orders,Order_details,admin
from django.http import HttpResponse, JsonResponse
import json
from django.db import IntegrityError
# Show all field---------------------------------------------
def W(request):
    words = Customers.objects.all()
    word_list = []
    for word in words:
        word_dict = {'name': word.name, 'age': word.age}
        word_list.append(word_dict)
    return JsonResponse(word_list, safe=False)

# ------------------------------------------------------------
# Customers Edit-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def serch_field_Customer(request , first_name):
    try:
        words = Customers.objects.filter(first_name=first_name) # فیلتر کردن بر اساس first_name
        word_list = []
        for word in words:
            word_dict = {'first_name': word.first_name, 'last_name': word.last_name,'email':word.email,'phone number': word.phone_number, 'Address': word.Address,'City':word.City, 'State': word.state,'postal_Code':word.postal_Code }
            word_list.append(word_dict)
        return JsonResponse(word_list, safe=False)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)




def add_field_Customer(request, first_name, last_name, email, phone_number, Address, City, state, postal_Code):
    new_word = Customers(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, Address=Address, City=City, state=state, postal_Code=postal_Code)
    new_word.save()
    return HttpResponse(''+first_name+' added successfully!')


def Delete_field_Customer(request, first_name):
    categories = Customers.objects.filter(first_name=first_name)
    count_before_delete = categories.count()
    for category in categories:
        category.delete()
    return HttpResponse(f"All {count_before_delete} categories with the name '{first_name}' were successfully deleted.")

def Update_field_Customer(request,first_name,last_name,email,phone_number,Address,City,state,postal_Code):
    customers = Customers.objects.filter(first_name=first_name)
    count_before_update = customers.count()
    for customer in customers:
        customer.last_name = last_name
        customer.email = email
        customer.phone_number = phone_number
        customer.Address = Address
        customer.City = City
        customer.state = state
        customer.postal_Code = postal_Code
        customer.save()
    return HttpResponse(f'{count_before_update} {first_name} updated successfully!')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Products Edit-----------------------------------------------------------------------------------------------------------------------------------------

def serch_field_Products(request, Product_name):

    try:
        words = Products.objects.filter(Product_name=Product_name) # فیلتر کردن بر اساس first_name
        word_list = []
        for word in words:
            word_dict = {'Product_name': word.Product_name, 'description': word.description,'price':word.price,'image': word.image}
            word_list.append(word_dict)
        return JsonResponse(word_list, safe=False)
    except Products.DoesNotExist:
        return HttpResponse(status=404) 

def add_field_Products(request, Product_name, description, price, image, category_id_id):
  try:
      new_word = Products(Product_name=Product_name, description=description, price=price, image=image, category_id_id=category_id_id)
      new_word.save()
      return HttpResponse(''+Product_name+' added successfully!')
  except IntegrityError as e:
    if 'FOREIGN KEY constraint failed' in str(e):
        return HttpResponse("The category you selected <b>does not exist</b>")
    else:
        # handle other types of IntegrityError or re-raise the exception
        pass
def delete_field_Products(request, Product_name):
    Delete_field = Products.objects.filter(Product_name=Product_name)
    De=Delete_field.count()
    for a in Delete_field :
     a.delete()
    return HttpResponse(f' {De} The '+Product_name+' was successfully deleted')

def Update_field_Products(request, Product_name, description, price, image, category_id_id):
    product = Products.objects.filter(Product_name=Product_name)
    p = product.count()
    for a in product :
        product.description = description
        product.price = float(price)
        product.image = image
        product.category_id_id = category_id_id
        a.save()
    return HttpResponse(f'{p}--{Product_name} Updated successfully!')

# ---------------------------------------------------------------------------------------------------------------------------------------------------
# categories Edit----------------------------------------------------------------------------------------------------------------------------------------

def serch_field_Categories(request, category_name):
    try:
        words = Categories.objects.filter(category_name=category_name)
        word_list = []
        for word in words:
         word_dict = {'categories_name': word.category_name,'category_description': word.category_description,'category_image':word.category_image}
         word_list.append(word_dict)
        return JsonResponse(word_list,safe=False)
    except Products.DoesNotExist:
        return HttpResponse(status=404)    

def add_field_Categories(request, category_name, category_description, category_image):
  try:
      new_word = Categories(category_name=category_name, category_description=category_description, category_image=category_image)
      new_word.save()
      return HttpResponse(''+category_name+' added successfully!')
  except IntegrityError as e:
    if 'FOREIGN KEY constraint failed' in str(e):
        return HttpResponse("The category you selected <b>does not exist</b>")
    else:
        # handle other types of IntegrityError or re-raise the exception
        pass
def delete_field_Categories(request, category_name):
    categories = Categories.objects.filter(category_name=category_name)
    for category in categories:
        category.delete()
    return HttpResponse('All ' + str(len(categories)) + ' categories with the name "' + category_name + '" were successfully deleted')

def Update_field_Categories(request, category_name, category_description, category_image):
    try:
        categories = Categories.objects.filter(category_name=category_name)
        c=categories.count()
        if categories:
            for category in categories:
                category.category_description = category_description
                category.category_image = category_image
                category.save()
            return HttpResponse(f'{c}---{category_name} updated successfully!')
        else:
            return HttpResponse(f'Category named {category_name} does not exist.')
    except Categories.DoesNotExist:
        return HttpResponse(f'Category named {category_name} does not exist.')


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Orders Edit--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def serch_field_Orders(request, Order_id):
    try:
        word = Orders.objects.filter(Order_id=Order_id)
        mylist = []
        for a in word:
          word_dict = {'Order_id': a.Order_id,'Customer_id': a.Customer_id_id,'Order_date':a.Order_date,'total_amount':a.total_amount,'payment_type':a.payment_type,'state':a.state}
          mylist.append(word_dict)
        return JsonResponse(mylist , safe=False)
    except Products.DoesNotExist:
        return HttpResponse(status=404)    

def add_field_Orders(request, Customer_id_id, Order_date, total_amount,payment_type,state):
  try:
      new_word = Orders(Customer_id_id=Customer_id_id, Order_date=Order_date, total_amount=total_amount,payment_type=payment_type,state=state)
      new_word.save()
      return HttpResponse('order to id'+total_amount+' added successfully!')
  except IntegrityError as e:
    if 'FOREIGN KEY constraint failed' in str(e):
        return HttpResponse("The category you selected <b>does not exist</b>")
    else:
        # handle other types of IntegrityError or re-raise the exception
        pass
def delete_field_Orders(request, Order_id):
    categories = Orders.objects.filter(Order_id=Order_id)
    for category in categories:
        category.delete()
    return HttpResponse('All ' + str(len(categories)) + ' categories with the name "' + Order_id + '" were successfully deleted')

def Update_field_Orders(request,Order_id, Customer_id_id, Order_date, total_amount,payment_type,state):
    Order = Orders.objects.get(Order_id=Order_id)
    Order.Customer_id_id = Customer_id_id
    Order.Order_date = Order_date
    Order.total_amount = total_amount
    Order.payment_type = payment_type
    Order.state = state
    Order.save()
    return HttpResponse(''+Order_id+' ❤️Updated successfully!❤️')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Order_details------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def serch_field_Order_details(request, Order_name):
    try:
        word = Order_details.objects.filter(Order_name=Order_name)
        my = []
        for a in word :
         word_dict = {'quantity': a.quantity,'item_notes':a.item_notes,'item_price':a.item_price,'item_status':a.item_status,'item_total':a.item_total,'item_discount':a.item_discount,'Order_id_id':a.Order_id_id,'Product_id_id':a.Product_id_id,'name':a.Order_name}
         my.append(word_dict)
        return JsonResponse(my , safe=False)
    except Products.DoesNotExist:
        return HttpResponse(status=404)    

def add_field_Order_details(request, quantity, item_notes, item_price,item_status,item_total, item_discount, Order_id_id, Product_id_id,Order_name):
  try:
      new_word = Order_details(quantity=quantity, item_notes=item_notes, item_price=item_price,item_status=item_status,item_total=item_total,item_discount=item_discount,Order_id_id=Order_id_id,Product_id_id=Product_id_id,Order_name=Order_name)
      new_word.save()
      return HttpResponse('Order_details to id'+Order_name+' added successfully!')
  except IntegrityError as e:
    if 'FOREIGN KEY constraint failed' in str(e):
        return HttpResponse("The category you selected <b>does not exist</b>")
    else:
        # handle other types of IntegrityError or re-raise the exception
        pass
def delete_field_Orders_details(request, Order_name):
    categories = Order_details.objects.filter(Order_name=Order_name)
    for category in categories:
        category.delete()
    return HttpResponse('All ' + str(len(categories)) + ' categories with the name "' + Order_name + '" were successfully deleted')

def Update_field_Orderss_details(request, quantity, item_notes, item_price, item_status, item_total, item_discount, Order_id_id, Product_id_id, Order_name):
    order = Order_details.objects.get(Order_name=Order_name)
    order.Order_id_id = Order_id_id
    order.Product_id_id = Product_id_id
    order.item_discount = item_discount
    order.item_total = item_total
    order.item_status = item_status
    order.item_price = item_price
    order.item_notes = item_notes
    order.quantity = quantity
    order.Order_name = Order_name
    order.save()
    return HttpResponse(f"{Order_name} ❤️Updated successfully!❤️")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#Customer Login-------------------------------------------------------------------------------------------------------------------------------------------------
def Login_Customer(request, **kwargs):
    first_name = kwargs.get('first_name', '')
    last_name = kwargs.get('last_name', '')
    email = kwargs.get('email', '')

    try:
        customer = Customers.objects.get(first_name=first_name, last_name=last_name, email=email)
        return HttpResponse("OK")
    except Customers.DoesNotExist:
        return HttpResponse("No")

def Login_admin(request, **kwargs):
    Usname = kwargs.get('Usname', '')
    password = kwargs.get('password', '')

    try:
        a = admin.objects.get(Usname=Usname, password=password)
        return HttpResponse("OK")
    except admin.DoesNotExist:
        return HttpResponse("No")