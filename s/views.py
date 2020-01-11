from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from django.template.loader import render_to_string
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

        return redirect('home') 
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def home(request):

    message ='See me?'
    return render(request,"home.html",{"message":message})

@login_required(login_url="/accounts/login/")
def logout_request(request):
    '''
    view function renders home page once logout
    '''
    logout(request)
    return redirect('home')
