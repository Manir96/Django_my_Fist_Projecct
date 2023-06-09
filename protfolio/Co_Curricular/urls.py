from django.urls import path
from . import  views

urlpatterns = [
    path('coc/', views.co_curricular),
   
]
