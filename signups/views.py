from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import SignUpForm

# Create your views here.

def home(request):

	#if request.method == 'POST':

	form = SignUpForm(request.POST or None)


	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		#send_mail(subject, message, from_email, to_list, fail_silently=True)
	
		subject = "Thank you for joining!!!"
		message = 'Wellcom to Us! \n We will meet soot!'
		from_email = settings.EMAIL_HOST_USER
		to_list = [save_it.email, settings.EMAIL_HOST_USER]

		send_mail(subject,message,from_email,to_list, fail_silently=True)	
		messages.success(request,'Thanks you for joining')
		return HttpResponseRedirect('/thanks/')

	form = SignUpForm()

	return render_to_response('signup.html', locals(), 
							   context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('thanks.html', locals(), 
							   context_instance=RequestContext(request))


def aboutus(request):
	return render_to_response('aboutus.html', locals(), 
							   context_instance=RequestContext(request))

