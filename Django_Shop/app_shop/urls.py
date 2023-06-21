from django.urls import path
from . import views

urlpatterns = [
#URls Customer---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     path('serch_fild_Customer/<str:first_name>/', views.serch_field_Customer, name='serch_fild_Customer'),
     path('add_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.add_field_Customer, name='add_field_Customer'),
     path('Delete_field_Customer/<str:first_name>/', views.delete_field_Customer, name='Delete_field_Customer'),
     path('Update_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.Update_field_Customer, name='Update_field_Customer'),
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
     path('serch_fild_/<str:first_name>/', views.serch_field_Products, name='serch_fild_Customer'),
     path('add_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.add_field_Products, name='add_field_Customer'),
     path('Delete_field_Customer/<str:first_name>/', views.delete_field_Products, name='Delete_field_Customer'),
     path('Update_field_Customer/<str:first_name>/<str:last_name>/<str:email>/<str:phone_number>/<str:Address>/<str:City>/<str:state>/<str:postal_Code>/', views.Update_field_Products, name='Update_field_Customer'),
    ]