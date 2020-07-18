from django.shortcuts import render

from pypro.modulos import facade


# views de classe base
def home(request):
    return render(request, 'base/home.html')

