from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def index(request):
	EMPS=Employee.objects.all
	context={'Employee':EMPS}
	return render(request,"base.html",context)

def CreateEMP(request):
	if request.method=='POST':
	    form = EmployeeForm(request.POST, use_required_attribute=False)

	    if form.is_valid():
	        form.save()
	        form = EmployeeForm()

	    context = {'form': form}
	    return redirect('/add/')
	form = EmployeeForm()

	context = {'form': form}
	return render(request, "empcreate.html", context)


