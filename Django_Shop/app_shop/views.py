from django.shortcuts import render
from .models import Customers
from django.http import HttpResponse, JsonResponse

def W(request):
    words = Customers.objects.all()
    word_list = []
    for word in words:
        word_dict = {'name': word.name, 'age': word.age}
        word_list.append(word_dict)
    return JsonResponse(word_list, safe=False)
def get_word(request, id):
    try:
        word = Customers.objects.get(id=id)
        word_dict = {'name': word.name, 'age': word.age}
        return JsonResponse(word_dict)
    except Customers.DoesNotExist:
        return HttpResponse(status=404)
def add_word(request,firs_name,last_name):
    new_word = Customers(firs_name=firs_name,last_name=last_name)
    new_word.save()
    return HttpResponse('Word added successfully!')