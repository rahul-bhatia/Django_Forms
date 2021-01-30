from django.shortcuts import render
from .form import InquiryForm

# Create your views here.

def home(request):
	fm=InquiryForm()
	if request.POST.get('name'):
		name=(request.POST.get('name'))
		email=(request.POST.get('email'))
		phone=(request.POST.get('phone'))
		print(name,email,phone)
		return render(request,'home.html',{'fm':fm,'msg':'Thank You '+name+" We will get back to you soon!"})
	return render(request,'home.html',{'fm':fm})
