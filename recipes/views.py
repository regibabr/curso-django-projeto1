from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return render(request, 'me-apague/temp.html')

def sobre(Request):
    return HttpResponse('sobre')