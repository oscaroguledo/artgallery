from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import CustomUser

# Create your views here.



class LoginView(View):
    def get(self, request):
        context = {"user":request.user}
        return render(request, 'authentication/login.html', context)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']

        context = {'values': request.POST}
        if email and password:
            username = CustomUser.objects.get(email=email).username
            user = auth.authenticate(username=username,email=email, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, f'Welcome! {user.username}, You are '
                                              f'now logged in.')
                print(request.POST, request.META['HTTP_REFERER'], '------------------')
                url = str(request.META['HTTP_REFERER'])
                if '/login/?next=' in url:
                    url = url.replace('/accounts/login/?next=', '')
                    print(url, '==============', request.META['HTTP_REFERER'])
                    return HttpResponseRedirect(url)
                else:
                    return redirect('home')

            if len(CustomUser.objects.filter(email=email)) == 0:
                context['email_errors'] = True
            else:
                context['email_errors'] = False
            if len(CustomUser.objects.filter(password=password)) == 0:
                context['pwd_errors'] = True
            else:
                context['pwd_errors'] = False
            messages.error(request, f'Invalid Credentials, Check Your details..')
            return render(request, 'authentication/login.html', context=context)

        messages.error(request, 'Please fill all fields')
        return render(request, 'authentication/login.html', context)
    
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


