from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def exprience(request):
    return render(request, 'exprience/exprience.html')