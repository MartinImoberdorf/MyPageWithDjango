from django.shortcuts import render
from aboutme.models import AboutMe
# Create your views here.
def aboutme(request):
    aboutme=AboutMe.objects.all()
    return render(request,"aboutme/aboutme.html",{"aboutme":aboutme})