from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("HI Dear")

def webpage(request):
    return render(request, "basic_web_page.html")