from django.shortcuts import render
from django.http import HttpResponseRedirect
import sendgrid
import os
from sendgrid.helpers.mail import *

def index(request):       
	return render(request, 'portfolio/index.html')



