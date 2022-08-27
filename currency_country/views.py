from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST','PUT'])
def country(request):
    if request.method == 'GET':
        return HttpResponse('<h1>GET METHOD</h1>')
    elif request.method == 'POST':
        return HttpResponse('<h1>POST METHOD</h1>')
    elif request.method == 'PUT':
        return HttpResponse('<h1>PUT METHOD</h1>')
    
    pass
