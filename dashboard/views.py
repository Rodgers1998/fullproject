from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm
from django.http import HttpResponse, HttpResponseRedirect
import requests
# Create your views here.

def home(request):
    return render(request,'dashboard/home.html')



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context={
            'form': form
        }
    return render(request,"dashboard/register.html",context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

@login_required
def co_workingspace(request):
    return redirect('https://iconshub.co.ke/bookings/')

@login_required
def icons_errands(request):
    return redirect('https://iconz.co.ke/')

@login_required
def icons_escapades(request):
    return redirect('https://iconshub.co.ke/events-images/')

@login_required
def icons_events(request):
    return redirect('https://iconshub.co.ke/events-images/')

@login_required
def icons_marketing(request):
    return redirect('https://iconshub.co.ke/events-images/')

@login_required
def dashboard_kenya(request):
    return redirect('https://www.facebook.com/iconshubke')

@login_required
def icons_whatsapp(request):
    return redirect('https://www.facebook.com/iconshubke')

@login_required
def icons_youtube(request):
    return redirect('https://www.youtube.com/channel/UCihJQT6jk6u9L-nUfO0gYoA')