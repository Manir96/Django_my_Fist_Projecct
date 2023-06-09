from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def co_curricular(request):
    return render(request, 'co_curricular/co_curricular.html')