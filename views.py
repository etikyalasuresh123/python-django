from django.shortcuts import render,redirect
from website1.forms import EmployeeForm,SignUpForm
from website1.forms import EmployeeForm
from website1.models import Employee
from django.urls import reverse_lazy


from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

def home_page(request):
	return render(request,'website1/home.html')

def signup_view(request):
	form=SignUpForm()
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.set_password(user.password)
			user.save()
			return HttpResponseRedirect('/accounts/login')
	return render(request,'website1/signup.html',{'form':form})   



class EmployeeListView(ListView):
	model=Employee

class EmployeeDetailView(DetailView):
	model=Employee

class EmployeeCreateView(CreateView):
 	model=Employee
 	fields='__all__'
 	success_url=reverse_lazy('employee_list') 

class EmployeeUpdateView(UpdateView):
	model=Employee
	fields=('name','age','esal','eaddr')
	success_url=reverse_lazy('employee_list') 

class EmployeeDeleteView(DeleteView):
	model=Employee
	success_url=reverse_lazy('employee_list')  
