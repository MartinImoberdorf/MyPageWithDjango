from django.contrib import admin
from .models import AboutMe

# Register your models here.

#Para que nos muestre pero solo de lectura nuestro registros updated y created 
class AboutMeAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

#Registramos
admin.site.register(AboutMe,AboutMeAdmin)