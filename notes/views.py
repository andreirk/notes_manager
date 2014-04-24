# -*- coding: utf-8 -*-

import datetime


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from forms import NoteAddForm


from notes.models import Category, Note


def index(request, page_number=1):
    # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question for p in latest_poll_list])
    # return HttpResponse(output)

    latest_note_list = []
    for note in Note.objects.all():
    	if note.author.username == auth.get_user(request).username:
    		latest_note_list.append(note)

    current_page = Paginator(latest_note_list, 3) 
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(template.render(context))
    context = {'latest_note_list': current_page.page(page_number), "username":auth.get_user(request).username}

    return render_to_response('notes/index.html', context)

def add_note(request):
	
	if request.POST:
		user = auth.get_user(request)
		form = NoteAddForm(request.POST)
		if form.is_valid():
			note = form.save(commit=False)
			note.pub_date = datetime.datetime.now()
			note.author = user
			form.save()
			request.session.set_expiry(3800)
			# request.session['pause'] = True
		return redirect('/notes/note/%s/' % note.id)
	else:
		username = auth.get_user(request).username
		note_form = NoteAddForm
		args = {}
		args.update(csrf(request))
		args['form'] = note_form
		args['username'] = username
		return render_to_response('notes/add_note.html',args)



def note(request, note_id):
	username = auth.get_user(request).username
	context = {"note": Note.objects.get(id = note_id),'username':username}
	return render_to_response('notes/note.html', context)


def change_note(request,note_id):
	args = {}
	args.update(csrf(request))
	old_note = Note.objects.get(pk=note_id)
	data = {'title': old_note.title,
			 'content':old_note.content,
			 'category':old_note.category,
			 'is_chosen':old_note.is_chosen,
			 'is_published':old_note.is_published,
			 'pub_date':old_note.pub_date,
			 'author':old_note.author}
	form = NoteAddForm(initial=data)
	args['form'] = form
	if request.POST:
		new_note_form = NoteAddForm(request.POST)
		if new_note_form.is_valid():
			new_note = new_note_form.save(commit=False)
			new_note.pub_date = old_note.pub_date
			new_note_form.save()
		return redirect('/notes/note/%s/' % note.id)
	else:
		return render_to_response("notes/change_note.html", args)








