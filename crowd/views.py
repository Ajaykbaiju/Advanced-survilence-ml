from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from  django.core.files.storage import FileSystemStorage
from urllib.parse import urlencode
from .models import *
from django.db.models import Sum
from django.db.models import Q
from abnormal_activity_detection import live
from abnormal_activity_detection import track

from keras import backend as K


def start_abnormal_activity(request):
    K.clear_session()
    result = live.detect_abnormal_activity()
    K.clear_session()
    return render(request,"admin/cam1.html",{'result':result})

def start_tracking(request):
    detected_faces = track.recognize_faces()
    return render(request,"admin/cam1.html",{'detected_faces':detected_faces})
    

def first(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"admin/index.html")

def index(request):
    return render(request,"index.html")

def register(request):
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")

def addlogin(request):
    st_name = request.POST.get('st_name')
    st_id = request.POST.get('st_id')
    password = request.POST.get('password')
    

    if station_regtable.objects.filter(st_name=st_name,st_id=st_id,password=password).exists():
            userdetails=station_regtable.objects.get(st_name=st_name,st_id=st_id, password=password)
            request.session['sid'] = userdetails.id
            request.session['st_name'] = userdetails.st_name
            return render(request,'admin/index.html')
    
    
    else:
        return render(request, 'login.html', {'msg':'Invalid Credentials'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)


def addregister(request):
    if request.method == "POST":
        a = request.POST.get('st_name')
        b = request.POST.get('st_id')
        h = request.POST.get('password')
        i = request.POST.get('cpassword')
        
        # Check if the email already exists in the regtable
        if station_regtable.objects.filter(st_id=b).exists():
            # Email already exists, display an alert message
            return render(request, 'register.html', {'msg': 'Station Id already exists. Please use a different Station Id.'})
        
        # Check if the entered password matches the confirm password
        if h != i:
            # Passwords don't match, display an alert message
            return render(request, 'register.html', {'msg1': 'Passwords do not match. Please re-enter the same password in confirm password.'})
        
        # Passwords match, proceed with inserting the data into the table
        ins = station_regtable(st_name=a, st_id=b, password=h)
        ins.save()
        
        return render(request, 'index.html', {'msg': 'Successfully Registered'})

    return render(request, 'register.html')




def cam1(request):
    if request.method=='POST':
        c=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(c.name,c)
        ins=cam1tbl(image=file)
        ins.save()    
    return render(request,"admin/cam1.html")

def cam2(request):
    if request.method=='POST':
        c=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(c.name,c)
        ins=cam2tbl(image=file)
        ins.save()
        K.clear_session()
        result = live.detect_abnormal_activity(cam_mode="./media/"+file)
        K.clear_session()
        return render(request,"admin/cam1.html",{'result':result})
    return render(request,"admin/cam2.html")

def cam3(request):
    if request.method=='POST':
        c=request.FILES['image']
        fs=FileSystemStorage()
        file=fs.save(c.name,c)
        ins=cam3tbl(image=file)
        ins.save()    
    return render(request,"admin/cam3.html")


