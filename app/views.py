from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_Topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('data is inserted')
        
        
    return render(request,'insert_Topic.html',d)


def insert_Webpage(request):
    WMFO=WebPageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFOD=WebPageModelForm(request.POST)
        if WMFOD.is_valid:
            WMFOD.save()
            return HttpResponse('data is inserted')
    return render (request,'insert_Webpage.html',d)


def insert_AccessRecord(request):
    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}
    if request.method=='POST':
        ARMFOD=AccessRecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse('data is inserted')
    return render(request,'insert_AccessRecord.html',d)
