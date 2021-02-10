from django.shortcuts import render

from .models import Tours
# Create your views here.

def index(request):

    ts = Tours.objects.all()    

    return render(request, 'index.html', {'ts': ts})