from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from account.models import CustomUser

# Create your views here.
#####=======================================

class GalleryView(View):
    def get(self, request):
        context = {"user":request.user}
        return render(request, 'gallery/gallery.html', context)

class GalleryFilter(View):
    def post(self, request):
        context = {"user":request.user}
        return render(request, 'gallery/gallery.html', context)
  