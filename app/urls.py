from django.urls import path
from .views import HomeView, PostDetail, AddPost, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('post/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('add_post/', AddPost.as_view() ,name='add_post'),
    path('update_post/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
        
]

