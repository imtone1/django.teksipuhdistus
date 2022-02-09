from django.shortcuts import render, redirect

# from .models import Teksti
from django.contrib.auth import authenticate, login, logout

from app.models import Teksti

def indexview(request):
    return render(request, "index.html")

def tekstipuhdistusview(request):
    return render(request, "tekstipuhdistus.html")

def tekstialkuperainen_get(request):
    teksti=request.POST['alkuperainenteksti']
    deletel=request.POST['delete_list']
    #jos on kirjoitettu monta sanaa välilyönnillä erotettuna, lisätään nämä listalle
    delete_lista=[]
    try:
        poista=deletel.split(",")
        for x in poista:
            if x !="":
                delete_lista.append(x)
    except:
        return render(request, "poikkeussivu.html")#exeption tai redirect sivustolle takaisin? LUo poikkeussivu!
# sql injektio tarkistus
    #tai suoraan
  
    for line in delete_lista:
        teksti=teksti.replace(line,"")
        teksti=teksti.replace("  ", " ")
        teksti1=teksti.strip() 

    context={'valmisteksti': teksti1}
    return render (request,"tekstipuhdistus.html",context)

# Loginpage
def loginview(request):
    return render (request, "loginpage.html")

def tietokantalistview(request):
    # if not request.user.is_authenticated:
    #     return render(request, 'loginpage.html')
    # else:
    tietokanta = Teksti.objects.all()
    
    context = {'tietokanta': tietokanta}
    return render (request,"editpage.html",context)

def addtekstitietokantaan(request):
    otsikko1 = request.POST['otsikko']
    teksti1 = request.POST['teksti']
    
    Teksti(otsikko = otsikko1, teksti=teksti1).save()
    return redirect(request.META['HTTP_REFERER'])

# def editsivulle(request):
#     return render(request, "editpage.html")

def deleteteksti(request, id):
    Teksti.objects.get(id = id).delete()
    return redirect(tietokantalistview)

def confirmdelete(request, id):
    tietokanta =Teksti.objects.get(id = id)
    context = {'tietokanta': tietokanta}
    return render (request,"deletepage.html",context)