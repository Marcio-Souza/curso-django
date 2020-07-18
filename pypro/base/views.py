from django.shortcuts import render


# views de classe base
def home(request):
    return render(request, 'base/home.html')
