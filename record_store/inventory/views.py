from django.http import HttpResponse
from django.shortcuts import render
from inventory.models import *

# Create your views here. - similar to controllers 

def index(request):

    artists = Artist.objects.all()

    return render(request, "inventory/index.html", locals())
