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
        
        #tacking data from forms
        username=request.POST['user_id']
        password=request.POST['password']
        #display in cmd
        print('uid:',username,' and ','pw:',password)
        
        #todisplay or fetch
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)
        
    return render(request,'insertion_form.html')

def insert_topic(request):
    if request.method=='POST':
        #tacking data from forms
        topic_name=request.POST['topic']
            #request.POST={'topic':'user inserted topic name'}
        #creating/inserting into database
        tog=Topic.objects.get_or_create(topic_name=topic_name)[0]
        tog.save()

        #todisplay or fetch
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        #tacking data from forms
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']

        #creating/inserting into database
        tog=Topic.objects.get(topic_name=topic_name)[0]
        tog.save()
        wog=Webpage.objects.get_or_create(topic_name=tog,name=name,url=url)[0]
        wog.save()        

        #todisplay or fetch
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_webpage.html')

def insert_access_record(request):
    if request.method=='POST':
        #taking data from forms
        topic_name=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        author=request.POST['author']
        date=request.POST['date']

        #creating/inserting into database
        tog=Topic.objects.get(topic_name=topic_name)[0]
        tog.save()
        wog=Webpage.objects.get(topic_name=tog,name=name,url=url)[0]
        wog.save()   
        aog=AccessRecord.objects.get_or_create(name=wog,author=author,date=date)[0] 
        aog.save()

        #todisplay or fetch
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'insert_access_record.html')

def update_topic(request):#rename
    if request.method=='POST':
        #tacking data from forms
        topic_name=request.POST['topic']
        new_topic=request.POST['newtopic']

        #rename topic_name
        Topic.objects.filter(topic_name=topic_name).update(topic_name=new_topic)
        
        #todisplay or fetch
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'update_topic.html')

def update_webpage(request):#rename
    if request.method=='POST':
        #TAKE DATA FROM FORMS
        topic=request.POST['topic']
        name=request.POST['name']
        new_name=request.POST['new_name']
        new_url=request.POST['new_url']
        #RENAME NAME
        tog=Topic.objects.get(topic_name=topic)#if web-object not present this is need to create
        Webpage.objects.update_or_create(name=new_name,defaults={'topic_name':tog,'url':new_url,})

        #DISPLAY DATA FROM DATABASE
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'update_webpage.html')

def update_access_record(request):#rename
    if request.method=='POST':
        #TAKE DATA FROM FORMS
        name=request.POST['name']
        author=request.POST['author']
        new_author=request.POST['new_author']
        new_date=request.POST['new_date']           
        #RENAME NAME
        wpo=Webpage.objects.get(name=name)
        AccessRecord.objects.update_or_create(author=new_author,defaults={'name':wpo,'date':new_date})
        
        #DISPLAY DATA FROM DATABASE
        tpo=Topic.objects.all()
        wpo=Webpage.objects.all()
        aro=AccessRecord.objects.all()
        d={'to':tpo,'wo':wpo,'ao':aro}
        return render(request,'display_db.html',d)

    return render(request,'update_access_record.html')
