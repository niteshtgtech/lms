import http
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import tbl_Authentication
    # Create your views here.
import random
from urllib import response
import django
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
# import local data
from .serializers import librarySerializer
from .models import libraryModel

# create a viewset
class libraryViewSet(viewsets.ModelViewSet):
	# define queryset

	queryset = libraryModel.objects.all()
	http_method_names = ['get','put','post', 'head', 'options', 'trace', 'delete']
	# specify serializer to be used
	serializer_class = librarySerializer
from django.shortcuts import render

# Create your views here.
import json
import requests
tib=[]
def index(request):
    books=models.libraryModel.objects.all()
    return render(request, "viewbook.html",{'main':books})

def books(request):                                                                                                    
    books=models.libraryModel.objects.all()
    return render(request, "pages/tables.html",{'main':books})

# name = models.CharField(max_length = 200)
#     author = models.CharField(max_length = 200)
#     description = models.TextField()
#     isbn
def create(request):
    if request.method == 'POST':
        nme=request.POST['nme']
        aut=request.POST['apsw']
        des=request.POST['dsw']
        rnd=random.randint(0,521212)
        nwdat=libraryModel(name=nme,author=aut,description=des,isbn=rnd)
        nwdat.save()
        return HttpResponseRedirect("books")

def delete(request):
    isbnid=request.GET['id']
    libraryModel.objects.filter(isbn=isbnid).delete()
    return HttpResponseRedirect("books")

def base(request):
    return render(request, 'base.html')
    

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        try:
            user = tbl_Authentication.empAuth_objects.get(username=username,password=password)
            if user is not None:               
                return render(request, 'dash.html', {})
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
    
                return redirect('/')
        except Exception as identifier:
            
            return redirect('/')
    
    else:
        return render(request, 'base.html')