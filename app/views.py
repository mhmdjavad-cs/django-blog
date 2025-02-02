from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post 
from django.urls import reverse_lazy



class HomeView(ListView):
    model = Post
    template_name = 'home_page.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = "__all__"
        

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'body')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home_page')




#def home_page(request):
#    return render(request, 'home_page.html', {})

#def hello(request):
#    return render(request, 'hello.html', {})
#    #return HttpResponse("hello world!!!")

