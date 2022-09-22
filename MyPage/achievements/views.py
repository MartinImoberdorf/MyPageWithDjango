from django.shortcuts import render
from achievements.models import Achievements
# Create your views here.
def achievements(request):
    achievements=Achievements.objects.all()
    return render(request,"achievements/achievements.html",{"achievements":achievements})