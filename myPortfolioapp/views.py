from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    home = Home.objects.latest('updated_at')
    about = About.objects.latest('updated_at')
    Categories=Category.objects.all()
    portfolios = Portfolio.objects.all()
    profiles= Profile.objects.latest('updated_stamp')
    context = {
        'home':home,
        'about':about,
        'categories':Categories,
        'portfolios':portfolios,
        'profiles':profiles,
    }
    return render(request,'index.html',context)