from django.shortcuts import render
from django.http import HttpResponse
from django.views import view
# Create your views here.
class MyView(view):
    def get(self,request):
        s1='<h1>Hello World</h1>'
        s2='<h1>Welcome</h1>'
        return HttpResponse(s1+s2)
    
