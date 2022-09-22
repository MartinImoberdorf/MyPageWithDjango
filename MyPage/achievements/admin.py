from django.contrib import admin
from .models import Achievements

# Register your models here.

#Para que nos muestre pero solo de lectura nuestro registros updated y created 
class AchievementsAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

#Registramos
admin.site.register(Achievements,AchievementsAdmin)