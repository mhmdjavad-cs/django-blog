from django.urls import path
from .views import HomeView, PostDetail, AddPost


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view() ,name='add_post'),
]

