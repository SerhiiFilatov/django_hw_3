from users.models import User_model
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def sign_in(request: HttpRequest)->HttpResponse:
    if request.method == 'POST':
        password = request.POST["password"]
        username = request.POST["username"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            redirect_url = reverse_lazy('home')
            return HttpResponseRedirect(redirect_url)
        return render(request, 'signin.html')
    return render(request, 'signin.html')


def sign_up(request: HttpRequest)->HttpResponse:
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'signup.html')
        try:
            User_model.objects.get(username=username)
            return render(request, 'signin.html')
        except User_model.DoesNotExist:
            User_model.objects.create_user(username=username, email=email, password=password)
        redirect_url = reverse_lazy("signin")
        return HttpResponseRedirect(redirect_url)
    return render(request, 'signup.html')


def logout_v(request: HttpRequest)->HttpResponse:
    logout(request)
    redirect_url = reverse_lazy('home')
    return HttpResponseRedirect(redirect_url)