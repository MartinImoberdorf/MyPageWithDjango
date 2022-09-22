from django.shortcuts import render, redirect
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    

    if request.method=="POST":
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            mensaje=request.POST.get("mensaje")


            email=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,mensaje),
            "",["imoberdorfmhhmm7@gmail.com"],reply_to=[email])

            try:
                email.send()

                return redirect("/opinions/?valido")
            except:
                return redirect("/opinions/?novalido")


    return render(request, "opinions/opinions.html", {})