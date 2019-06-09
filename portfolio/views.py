from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):       
	return render(request, 'portfolio/index.html')

def download(request):
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="portfolio.pdf"'
	return response

