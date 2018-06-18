from django.shortcuts import render
from django.http import HttpResponseRedirect
import os

def index(request):       
	return render(request, 'portfolio/index.html')



