from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from registration.forms import SignUpForm
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            guest_group = Group.objects.get(name='Guest')
            guest_group.user_set.add(user)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'guest/register.html', {'form': form})
