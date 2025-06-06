from django.shortcuts import render
from .models import BakeryInfo
from .models import Items
from .models import ContactInfo

# Create your views here.

def homeView(request):
    
    InfoDict = {
        'Info' : BakeryInfo.objects.first(),
    }
    return render(request, 'home.html', InfoDict)

def contactView(request):
    InfoDict = {
        'Info': ContactInfo.objects.first(),
        'BakeryInfo': BakeryInfo.objects.first()
    }

    return render(request, 'contact.html', InfoDict)

def galleryView(request):

    InfoDict = {
        'BakeryInfo': BakeryInfo.objects.first(),
        'GalleryItem' : Items.objects.all()
    }
    return render(request,'gallery.html', InfoDict)