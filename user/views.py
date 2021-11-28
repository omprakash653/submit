from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Post
from django.contrib import messages
# Create your views here.

def home(request):

    return render(request, 'user/index.html')

def user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        user = User.objects.create(
            username=username, firstname=first_name, lastname=last_name, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/')
    else:
        return render(request, 'user/user.html')

def post(request):
    if request.method == "POST":
        user = request.POST['username']
        text = request.POST['text']

        user = User.objects.get(username=user)
        post = Post(user=user, text=text)
        post.save()
        messages.success(request, 'posted successfully!')
    return render(request, 'user/post.html')
