from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post 


class HomeView(ListView):
    model = Post
    template_name = 'home_page.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'







#def home_page(request):
#    return render(request, 'home_page.html', {})

#def hello(request):
#    return render(request, 'hello.html', {})
#    #return HttpResponse("hello world!!!")

