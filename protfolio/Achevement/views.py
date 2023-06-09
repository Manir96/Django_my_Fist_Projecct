from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def achevement(request):
    return render(request, 'achevement/achevement.html')
