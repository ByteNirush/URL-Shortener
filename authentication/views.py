from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import RegisterForm

def register_view(request):
    #Register new user
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
            