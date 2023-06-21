from django.urls import path
from . import views

urlpatterns = [
     path('words/<int:id>/', views.get_word, name='get_word'),
     path('add_word/<str:firs_name>/<str:last_name>/', views.add_word, name='add_word'),
    ]