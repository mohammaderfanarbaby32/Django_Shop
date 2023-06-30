from django.urls import path
from . import views

urlpatterns = [
#URls Customer-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     path('serch_field_Customer/<str:first_name>/', views.serch_field_Customer, name='serch_fild_Customer'),
     path('add_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.add_field_Customer, name='add_field_Customer'),
     path('Delete_field_Customer/<str:first_name>/', views.Delete_field_Customer, name='Delete_field_Customer'),
     path('Update_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.Update_field_Customer, name='Update_field_Customer'),
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#URls Products-----------------------------------------------------------------------------------------------------------------------------------------------------------------------     
     path('serch_fild_Products/<str:Product_name>/', views.serch_field_Products, name='serch_field_Products'),
     path('add_field_Products/<str:Product_name>/<str:description>/<str:price>/<str:image>/<str:category_id_id>/', views.add_field_Products, name='add_field_Products'),
     path('delete_field_Products/<str:Product_name>/', views.delete_field_Products, name='delete_field_Products'),
     path('Update_field_Products/<str:Product_name>/<str:description>/<str:price>/<str:image>/<str:category_id_id>/', views.Update_field_Products, name='Update_field_Products'),
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#URls Categories-------------------------------------------------------------------------------------------------------------------------------------------------------------  
     path('serch_field_Categories/<str:category_name>/', views.serch_field_Categories, name='serch_field_Categories'),
     path('add_field_Categories/<str:category_name>/<str:category_description>/<str:category_image>/', views.add_field_Categories, name='add_field_Categories'),
     path('delete_field_Categories/<str:category_name>/', views.delete_field_Categories, name='delete_field_Categories'),
     path('Update_field_Categories/<str:category_name>/<str:category_description>/<str:category_image>/', views.Update_field_Categories, name='Update_field_Categories'), 
#----------------------------------------------------------------------s------------------------------------------------------------------------------------------------------  
#URls Orders------------------------------------------------------------------------------------------------------------------------------------------------------------- 
     path('serch_field_Orders/<str:Order_id>/', views.serch_field_Orders, name='serch_field_Orders'),
     path('add_field_Orders/<str:Customer_id_id>/<str:Order_date>/<str:total_amount>/<str:payment_type>/<str:state>/', views.add_field_Orders, name='add_field_Orders'),
     path('delete_field_Orders/<str:Order_id>/', views.delete_field_Orders, name='delete_field_Orders'),
     path('Update_field_Orders/<str:Order_id>/<str:Customer_id_id>/<str:Order_date>/<str:total_amount>/<str:payment_type>/<str:state>/', views.Update_field_Orders, name='Update_field_Orders'),   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#URls Order_details-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     path('serch_field_Order_details/<str:Order_name>/', views.serch_field_Order_details, name='serch_field_Order_details'),
     path('add_field_Order_details/<str:Order_id_id>/<str:Product_id_id>/<str:Order_name>/<str:quantity>/<str:item_notes>/<str:item_price>/<str:item_discount>/<str:item_total>/<str:item_status>/', views.add_field_Order_details, name='add_field_Order_details'),
     path('delete_field_Orders_details/<str:Order_name>/', views.delete_field_Orders_details, name='delete_field_Orders_details'),
     path('Update_field_Orders_details/<str:Order_name>/<str:Product_id_id>/<str:Order_id_id>/<str:quantity>/<str:item_notes>/<str:item_price>/<str:item_discount>/<str:item_total>/<str:item_status>/', views.Update_field_Orderss_details, name='Update_field_Orderss_details'),   
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
     path('Login_Customer/<str:first_name>/<str:last_name>/<str:email>/', views.Login_Customer, name='Login_Customer'),
     path('Login_admin/<str:Usname>/<str:password>/', views.Login_admin, name='Login_admin'),      
#------------------------------------------------------------------------------------------------------------------------
#Customers can browse products by category and view details of each product-----------------------------------
     path('products_by_category/<str:category_id_id>/', views.products_by_category, name='products_by_category'),
#-------------------------------------------------------------------------------------------------------------
#Cart_C-------------------------------------------------------------------------------------------------
path('Cart_C/<str:Customer_id_id>/<str:Product_id_id>/<str:Number>/', views.Cart_C , name='Cart_C'),
#-------------------------------------------------------------------------------------------------------
#Cart_D-----------------------------------------------------
path('Cart_D/<str:Cart_id>/', views.Cart_D , name='Cart_D'), 
#-----------------------------------------------------------
#Cart_U-----------------------------------------------------------------------------------------------------------
path('Cart_U/<str:Cart_id>/<str:Product_id_id>/<str:Number>/<str:Customer_id_id>/', views.Cart_U , name='Cart_U'),
#------------------------------------------------------------------------------------------------------------------
#Cart_ALL--------------------------------------------
path('Cart_ALL/', views.Cart_ALL , name='Cart_ALL'),
#----------------------------------------------------
#Empty_the_shopping_cart--------------------------------------------
path('Empty_the_shopping_cart/<str:Cart_id>/<str:Customer_id_id>/<str:quantity>/<str:item_notes>/<str:Product_id_id>/<str:Order_name>/<str:item_price>/<str:item_discount>/<str:item_total>/<str:item_status>/<str:Order_date>/<str:total_amount>/<str:payment_type>/<str:state>/<str:Order_id_id>/', views.Empty_the_shopping_cart , name='Empty_the_shopping_cart'),
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#order_history_and_order_status------------------------------------------------------------------------------------------------------------
path('order_history_and_order_status/<str:Customer_id_id>/', views.order_history_and_order_status, name='order_history_and_order_status'),
#The_end-------------------------------------------------------------------------------------------------------------------------------------------
    ]                                                                     