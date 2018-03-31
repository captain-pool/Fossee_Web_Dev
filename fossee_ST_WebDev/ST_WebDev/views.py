from django.shortcuts import render
from django.http import HttpResponse
from ST_WebDev.models import user
# Create your views here.
def index(request):
    usr=user.objects.all()
    return render(request,'index.html',{'Name':'Adrish','usrlist':usr})
