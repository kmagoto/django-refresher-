from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from classchedule.models import PersonalData

# Create your views here.

def kusoma(request):
    return render(request, 'website/welcome.html',
                  {"studentnumbers": PersonalData.objects.count})

def datetoday(request):
    return HttpResponse('Todays date is: '+ str(datetime.now()))

def eshop(request):
    return HttpResponse('Constant practice is key!')