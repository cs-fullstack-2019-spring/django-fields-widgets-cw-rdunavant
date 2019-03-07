from django.shortcuts import render
from django.http import HttpResponse
from .forms import ApplicationForm

# Create your views here.
def index(request):
    if(request.method=="POST"):
        form=ApplicationForm(request.POST)
    return render(request, "App/index.html", {"form": ApplicationForm()})