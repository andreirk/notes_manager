# -*- coding: utf-8 -*-

import datetime


from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from forms import NoteAddForm
from models import Note


from notes.models import Category, Note


def index(request, page_number=1):
    # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question for p in latest_poll_list])
    # return HttpResponse(output)

    latest_note_list = []

    for note in Note.objects.filter(is_published=True):

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
	args = {}
	args.update(csrf(request))
	username = auth.get_user(request).username
	args['username'] = username
	# TODO добавить валидацию формы, сейчас можно отправить пустую форму, и возникнет ощибка, 
	# это никак не обрабатывается
	if request.POST:
		user = auth.get_user(request)
		form = NoteAddForm(request.POST)
		
		if form.is_valid():
			note = form.save(commit=False)
			note.pub_date = datetime.datetime.now()
			note.author = user
			form.save()
			
			# request.session['pause'] = True
			return redirect('/notes/note/%s/' % note.id)
		else:
			error = 'Не корректные данные, проверьте правильность заполнения формы <br> (все поля должны быть заполнены)'
			new_note_form = NoteAddForm(request.POST)
			args['error'] = error
			args['form'] = new_note_form
			return render_to_response("notes/add_note.html", args)
	else:
		note_form = NoteAddForm
		args['form'] = note_form
		

		return render_to_response('notes/add_note.html',args)



def note(request, note_id):
	username = auth.get_user(request).username
	context = {"note": Note.objects.get(id = note_id),'username':username}
	return render_to_response('notes/note.html', context)


# a = Article.objects.get(pk=1)
#  f = ArticleForm(request.POST, instance=a)
#  f.save()

def change_note(request,note_id):
	username = auth.get_user(request).username
	args = {}
	args['username'] = username
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
	args['note_id'] = note_id
	if request.POST:
		new_note = get_object_or_404(Note, pk=note_id)
		new_note_form = NoteAddForm(request.POST, instance=new_note)
		if new_note_form.is_valid():
			
			# new_note.title = request.POST['title']
			# new_note.content = request.POST['content']
			# new_note.category.id = request.POST['category']
			# new_note.is_chosen = request.POST['is_chosen']
			# new_note.is_published = request.POST['is_published']
			new_note.save()

			return redirect('/notes/note/%s/' % new_note.id)
		else:
			error = 'Не корректные данные, проверьте правильность заполнения формы <br> (все поля должны быть заполнены)'
			new_note_form = NoteAddForm(request.POST)
			args['error'] = error
			args['form'] = new_note_form

			return render_to_response("notes/change_note.html", args)

	else:
		return render_to_response("notes/change_note.html", args)




def del_note(request,note_id):
	args = {}
	args.update(csrf(request))
	note = get_object_or_404(Note,pk=note_id)
	args['note'] = note
	if request.POST:
		note_to_del = get_object_or_404(Note, pk=request.POST['note_to_del'])
		note_to_del.delete()
		args['delete_success'] = True
		return render_to_response('notes/del_note.html/', args)
	else:
		return render_to_response('notes/del_note.html', args)


# def change_note(request,note_id):
# 	args = {}
# 	args.update(csrf(request))
# 	old_note = Note.objects.get(pk=note_id)
# 	data = {'title': old_note.title,
# 			 'content':old_note.content,
# 			 'category':old_note.category,
# 			 'is_chosen':old_note.is_chosen,
# 			 'is_published':old_note.is_published,
# 			 'pub_date':old_note.pub_date,
# 			 'author':old_note.author}
# 	form = NoteAddForm(initial=data)
# 	args['form'] = form
# 	args['note'] = old_note
# 	if request.POST:
# 		new_note_form = NoteAddForm(request.POST)
# 		if new_note_form.is_valid():
# 			new_note = new_note_form.save(commit=False)
# 			new_note.author = data['author']
# 			new_note.pub_date = data['pub_date']
# 			new_note_form.save()
# 			# new_note = get_object_or_404(Note,pk=note_id)
# 			# new_note.title = request.POST['title']
# 			# new_note.content = 'terlim bom bom'#request.POST['content']
# 			# new_note.category = request.POST['category']
# 			# new_note.is_chosen = request.POST['is_chosen']
# 			# new_note.is_published = request.POST['is_published']
# 			# new_note.save()
			
# 		return redirect('/notes/note/%s/' % new_note.id)
# 	else:
# 		return render_to_response("notes/change_note.html", args)
