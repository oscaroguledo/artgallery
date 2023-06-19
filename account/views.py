from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# Create your views here.
#####=======================================

def index(request):
    context = {}
    return render(request, 'index.html', context)

    
@login_required
def editprofile(request, email):
    if request.method == 'GET':
        
        return render(request, 'authentication/editprofile.html')

    elif request.method == 'POST':
        username = request.POST['username']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        email = request.POST['email']
        country = request.POST['country']
        phone_num = request.POST['phone_num']
        try:
            file = request.FILES['file']
        except Exception:
            pass
        
        instance = CustomUser.objects.get(email=email)
        

        instance.username = username
        instance.firstname = firstname
        instance.lastname = lastname
        instance.email = email
        instance.country = country
        instance.phone_num = phone_num
        try:
            instance.image = file
        except Exception:
            pass
        instance.save()

        messages.success(request, f'You have successfully Updated Your profile')
        return redirect('editprofile', email)


@login_required
def profile(request, email):
    profile = CustomUser.objects.get(email=email)

    context = {'profile': profile}
    return render(request, 'authentication/profile.html', context)


