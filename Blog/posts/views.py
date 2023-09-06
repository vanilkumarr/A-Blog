from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import url
from .models import Post
# Create your views here.

def index(request):
    posts =Post.objects.all()
    return render(request, 'index.html',dict(posts=posts))
def gost(request,pk):
    posts =Post.objects.get(id=pk)
    return render(request,"gost.html",dict(posts=posts))