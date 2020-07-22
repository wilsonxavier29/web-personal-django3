from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request);
return HttpResponse("<h1>mi web personal</h1><h2>portada</h2>")
