from django.shortcuts import render
from django.http import HttpResponse
TaxRate=15

def tax1(request):
    return render(request,"lap4/lapfour.html")

def tax2(request,num):
    num = num+(TaxRate/100*num)
    return HttpResponse(num)

def tax3(request):
    return render(request,"lap4/lap_four.html",{"TaxRate":TaxRate})
# Create your views here.
