from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            pass

    return render(request, 'authentication/login.html', {})
