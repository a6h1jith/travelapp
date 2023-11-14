from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import person
# Create your views here.
def home(request):
    var=place.objects.all()
    imp=person.objects.all()
    return render(request,'index.html',{'result':var , 'people':imp})
