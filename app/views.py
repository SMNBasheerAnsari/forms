from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def first_form(request):
    if request.method=='POST':
        return HttpResponse('data is inserted')

    return render(request,'insertion_form.html')

def insertion_form(request):
    if request.method=='POST':
        #render(request,'insert_topic.html')
        
        username=request.POST['user_id']
        password=request.POST['password']
        print('uid:',username,' and ','pw:',password)
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)
        
    return render(request,'insertion_form.html')

def insert_topic(request):
    if request.method=='POST':
        topic_name=request.POST['topic']

        tog=Topic.objects.get_or_create(topic_name=topic_name)[0]
        tog.save()

        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']

        tog=Topic.objects.get_or_create(topic_name=topic_name)[0]
        tog.save()
        wog=Webpage.objects.get_or_create(topic_name=tog,name=name,url=url)[0]
        wog.save()        

        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_webpage.html')

def insert_access_record(request):
    if request.method=='POST':
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        author=request.POST['author']
        date=request.POST['date']

        tog=Topic.objects.get_or_create(topic_name=topic_name)[0]
        tog.save()
        wog=Webpage.objects.get_or_create(topic_name=tog,name=name,url=url)[0]
        wog.save()   
        aog=AccessRecord.objects.get_or_create(name=wog,author=author,date=date)[0] 
        aog.save()

        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_access_record.html')