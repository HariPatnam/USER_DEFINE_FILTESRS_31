from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'my SelF hArI PaTnAm'}
    return render (request,'filters.html',d)
