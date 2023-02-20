from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def home(request):
    now = datetime.datetime.now()
    html = "<html><body style='font-family: Verdana, sans-serif;'>It is now %s</body></html>" % now
    return HttpResponse(html)
