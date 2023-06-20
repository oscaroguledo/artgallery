from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import Art, Attachment, CustomUser
import json
from django.core.paginator import Paginator


# Create your views here.
#####=======================================

class GalleryView(View):
    def get(self, request, type):
        art = Art.objects.all()
        painting = Art.objects.filter(type="painting")
        drawing = Art.objects.filter(type="drawing")
        nfts = Art.objects.filter(type="nfts")

        context = {"user":request.user,
                   "art":art,
                   "painting":painting}
        paginator = Paginator(art, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {"user":request.user,
                   "art":art,
                   "painting":painting,
                   "drawing":drawing,
                   "nfts":nfts,
                   'page_obj': page_obj, }
        print(painting,"==============================")
        return render(request, 'gallery/gallery.html', context)

def search_gallery(request):
    if request.method == 'POST':
        q = request.POST['q']
        
        art = Art.objects.filter(name__icontains=q, ) | \
                  Art.objects.filter(type__icontains=q, ) | \
                  Art.objects.filter(art_by__icontains=q, ) | \
                  Art.objects.filter(date_uploaded__icontains=q, )
        count = art.count
        print(q,"===========================", count)
        paginator = Paginator(art, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {'art': art,
                   'count': count,
                   'page_obj': page_obj, }
        return render(request, 'gallery/gallery.html', context)
    else:
        art = Art.objects.all()
        count = art.count
        paginator = Paginator(art, 5)
        page_number = request.GET.get('page')
        page_obj = Paginator.get_page(paginator, page_number)
        context = {'art': art,
                   'count': count,
                   'page_obj': page_obj, }
        return render(request, 'gallery/gallery.html', context)

        

  