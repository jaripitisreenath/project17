from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def brock(request):
    if request.method=='POST':
        TA=request.POST.get('tn')
        T=Topic.objects.get_or_create(Topic_name=TA)[0]
        T.save()
        return HttpResponse('INSRTED SUCCESSFULL')
    return render(request,'brock.html')

def naga(request):
    T=Topic.objects.all()
    d={'T':T}
    if request.method=='POST':
        Tp=request.POST['tn']
        wb=request.POST['WD']
        ur=request.POST['ul']
        T=Topic.objects.get_or_create(Topic_name=Tp)[0]
        T.save()
        W=Webpage.objects.get_or_create(Topic_name=T,Name=wb,URL=ur)[0]
        W.save()
        return HttpResponse('SUCCESSFULL')
        
    return render(request,'naga.html',d)
def roman(request):
    
    W=Webpage.objects.all()
    d={'w':W}
    if request.method=='POST':
         topic=request.POST['TP']
         name=request.POST['NM']
         url=request.POST['ur']
         dat=request.POST['dt']
         
         T=Topic.objects.get_or_create(Topic_name=topic)[0]
         T.save()
         W=Webpage.objects.get_or_create(Topic_name=T,Name=name,URL=url)[0]
         W.save()
         A=Access.objects.get_or_create(Topic_name=W,date=dat)[0]
         A.save()
    return render(request,'roman.html',d)
    