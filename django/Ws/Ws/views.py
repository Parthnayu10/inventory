from django.http import HttpResponse
from django.shortcuts import render
def aboutUs(request):
    # Your view logic here
    return HttpResponse("Hello, world!")

def homePage(request):
    return render(request,"index.html")