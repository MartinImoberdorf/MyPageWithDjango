from django.shortcuts import render,HttpResponse

def mystory(request):
    return render(request,"MyPageApp/mystory.html")

