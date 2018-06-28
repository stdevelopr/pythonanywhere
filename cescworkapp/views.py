from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Work
from .forms import WorkForm

# Create your views here.
def home(request):
	works = Work.objects.filter(status=True) #return all works from the database
	return render(request, 'home.html', {"works":works})

def work_detail(request, id):
	try:
		work = Work.objects.get(id=id)
	except Work.DoesNotExist:
		return redirect('/')
	return render(request, 'work_detail.html', {'work':work})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username = username, password=password)
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	form = UserCreationForm()
	context = {'form' :form}
	return render(request, 'registration/register.html', context)

@login_required(login_url='/')
def create_work(request):
	error = ''
	if request.method=='POST':
		work_form = WorkForm(request.POST, request.FILES)
		if work_form.is_valid():
			work = work_form.save(commit=False)
			work.user = request.user
			work.save()
			return redirect('my_works')
		else:
			error = "Data not valid"

	work_form = WorkForm()
	return render(request, 'create_work.html', {'error':error})


@login_required(login_url='/')
def edit_work(request, id):
	try:
		work= Work.objects.get(id=id, user=request.user)
		error = ''
		if request.method == 'POST':
			work_form = WorkForm(request.POST, request.FILES, instance=work)
			if work_form.is_valid():
				work.save()
				return redirect('my_works')
			else:
				error = 'Data is not valid'

		return render(request, 'edit_work.html', {'work':work, 'error':error})
	except Work.DoesNotExist:
		return redirect ('/')


@login_required(login_url='/')
def my_works(request):
	works = Work.objects.filter(user=request.user)
	return render(request, 'my_works.html', {"works":works})
