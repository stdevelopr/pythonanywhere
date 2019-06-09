from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import os

def index(request):
	return render(request, 'portfolio/index.html')

def download(request):
    with open('/home/stdevelopr/portfolio.pdf', 'rb') as pdf:
        path = '/home/stdevelopr/portfolio.pdf'
        response = FileResponse(open(path, 'rb'), content_type="application/pdf")
        response['Content-Disposition'] = 'attachment; filename="portfolio.pdf"'
        return response

