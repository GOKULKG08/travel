from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import team
#
def home(request):
    obj = place.objects.all()
    obj1 = team.objects.all()
    return render(request,'index.html',{'K':obj,'K1':obj1})

# def home1(request):

    # return render(request,'index.html',{'result1':obje})

# def addittion(request):
    # x=int(request.GET['num2'])
    # y=int(request.GET['num3'])
    # res1=x+y
    # res2=x-y
    # res3=x*y
    # res4=x/y

    # return render(request, 'index.html')



# def contact(request):
#     return HttpResponse('kggokul07@gmial.com')
# def detail(request)
#     return render(request,'result.html')
# def thanks(request):
#     return HttpResponse('thanks')
