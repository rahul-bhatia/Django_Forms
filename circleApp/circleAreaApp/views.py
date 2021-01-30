from django.shortcuts import render
from .form import ACFroms

# Create your views here.
def home(request):
	fm=ACFroms()
	if request.GET.get('radius'):
		r=float(request.GET.get('radius'))
		area=3.14*r*r
		circum=3.14*2*r
		msg="Area ="+str(round(area,2))+" Circumfrance="+str(round(circum,2))
		return render(request,'home.html',{'fm':fm,'msg':msg})
	
	return render(request,'home.html',{'fm':fm})