import sendgrid
import os
from sendgrid.helpers.mail import *
from django.http import HttpResponseRedirect
from django.shortcuts import render

def send(request):
	if request.method == 'POST':  
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		print(type(name))
		print(email)
		print(message)
		sg = sendgrid.SendGridAPIClient(apikey='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') #insert APIKEY
		from_email = Email(email)
		to_email = Email("stdevelopr@gmail.com")
		subject = "Website Message from"+" "+name
		content = Content("text/plain", message)
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		print(response.status_code)
		print(response.body)
		print(response.headers)

		request.session['form-submitted'] = True
		return HttpResponseRedirect('thanks/')
		# return render(request, 'portfolio/thanks.html')
	else:
		return HttpResponseRedirect('/')


def success(request):
	if request.session['form-submitted'] == True:
		request.session.flush()
		request.session['form-submitted'] = False
		return render(request, 'portfolio/thanks.html')
	else:
		return HttpResponseRedirect('/')