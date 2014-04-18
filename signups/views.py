from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import auth
from django.core.context_processors import csrf

from loginsys.forms import RegisterForm

# Create your views here.

def home(request):

	#if request.method == 'POST':

	form = RegisterForm(request.POST or None)
	username = auth.get_user(request).username
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		#send_mail(subject, message, from_email, to_list, fail_silently=True)
	
		subject = "Спасибо что вы с нами {0}".format(save_it.first_name)
		message = '<h1>Wellcom to Us!</h1> \n We will meet soot!'
		from_email = settings.EMAIL_HOST_USER
		to_list = [save_it.email, settings.EMAIL_HOST_USER]

		send_mail(subject,message,from_email,to_list, fail_silently=True)	
		messages.success(request,'Thanks you for joining {0}'.format(save_it.first_name))
		return HttpResponseRedirect('/thanks/')

	form = RegisterForm()

	return render_to_response('signup.html', locals(), 
							   context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('thanks.html', locals(), 
							   context_instance=RequestContext(request))


def aboutus(request):
	name = "save_it.first_name"
	return render_to_response('aboutus.html', locals(), 
							   context_instance=RequestContext(request))

