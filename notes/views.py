# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf



from notes.models import Category, Note


def index(request):
    # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    # output = ', '.join([p.question for p in latest_poll_list])
    # return HttpResponse(output)

    latest_note_list = Note.objects.all()[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(template.render(context))
    context = {'latest_note_list': latest_note_list, "username":auth.get_user(request).username}
    return render_to_response('notes/index.html', context)