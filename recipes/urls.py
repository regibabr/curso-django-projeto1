from django.urls import path
from django.http import HttpResponse
from recipes.views import home




urlpatterns = [
    
    path('', home),
   # path('contato/', contato),
   # path('sobre/', sobre),
]
