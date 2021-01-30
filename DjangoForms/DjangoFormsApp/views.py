from django.shortcuts import render
from .form import EoForm

# Create your views here.
def home(request):
	fm=EoForm()
	if request.GET.get('num'):
		res="Even" if int(request.GET.get('num'))% 2 ==0 else "Odd" 
		res=request.GET.get('num')+" is "+res
		print(res)
		return render(request,'home.html',{'fm':fm,'res':res})
	else:
		return render(request,'home.html',{'fm':fm})