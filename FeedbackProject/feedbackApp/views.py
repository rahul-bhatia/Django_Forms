from django.shortcuts import render
from .forms import FbForm

# Create your views here.
def home(request):
	if request.POST.get('name'):
		n=request.POST.get('name')
		fb=request.POST.get('feedback')
		fb1=FbForm()
		print(n,fb)
		return render(request,'home.html',{'fm':fb1,'msg':"Thanks "+n+" for your feedback"})
	else:
		fb=FbForm()
		return render(request,'home.html',{'fm':fb})