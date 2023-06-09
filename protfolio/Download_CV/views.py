from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def download_cv(request):
    return render(request, 'download/download.html')