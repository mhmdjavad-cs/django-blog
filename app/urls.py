from django.urls import path
from .views import hello, home_page


urlpatterns = [
    path('', home_page, name='home_page')
]

