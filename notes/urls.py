from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', 'notes.views.index', name='index'),

    url(r'^(?P<note_id>\d+)/$', 'note.views.detail', name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<note_id>\d+)/results/$', 'note.views.results', name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<note_id>\d+)/vote/$', 'note.views.vote', name='vote'),


    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
   
)