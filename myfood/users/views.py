from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import logout

# Create your views here.


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index:index')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

def profile_view(request):
    return render(request, 'users/profile.html')
