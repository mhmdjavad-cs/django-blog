from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html', {})



def hello(request):
    return render(request, 'hello.html', {})
    #return HttpResponse("hello world!!!")

