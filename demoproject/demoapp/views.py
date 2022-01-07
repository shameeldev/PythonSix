from django.http import HttpResponse
from django.shortcuts import render
from . models import Team
# Create your views here.
def home(request):
    obj = {'result' : Team.objects.all()}
    return render(request,'index.html',obj)

def details(request):
    return render(request,'details.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def thanks(request):
    return render(request,'thanks.html')

def operations(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])

    sum = x+y
    balance = x-y
    product = x*y
    division = x/y
    print('sum',sum)
    return render(request, 'thanks.html', {'sum' : sum, 'balance' : balance, 'product' : product, 'division' : division})