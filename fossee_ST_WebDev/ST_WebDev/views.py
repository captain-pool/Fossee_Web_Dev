from django.shortcuts import render
from django.db.models import Count
from ST_WebDev.models import user,foss,tutorial_detail,payment
# Create your views here.
mapmonth={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
	
def index(request):
	if request.method=='GET':
		return render(request,'index.html')
	if request.method=='POST':
		dates=[]
		try:
			month=request.POST['month']
			year=request.POST['yr']
			tutorial=tutorial_detail.objects.filter(actual_submission_date__year=year,actual_submission_date__month=month)
			for o in tutorial:
				obj={}
				obj['foss']=o.foss.name
				obj['courseName']=o.tutorial_name
				obj['actual_date']=o.actual_submission_date
				obj['expected_date']=o.expected_submission_date
				dates.append(obj)
			contrib=tutorial_detail.objects.filter(actual_submission_date__year=year,actual_submission_date__month=month).values('contributor').annotate(count=Count('contributor'))
			foss=[{'publisher':user.objects.filter(pk=x['contributor'])[0].name,'publishCount':x['count']} for x in contrib]
			return render(request,'index.html',{'dates':dates,'foss':foss,'month':mapmonth[int(month)],'year':year})
		except KeyError:
			return render(request,'index.html',{'err':1})