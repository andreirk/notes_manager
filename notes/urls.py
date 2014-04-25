from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', 'notes.views.index', name='index'),

    url(r'^note/(?P<note_id>\d+)/$', 'notes.views.note', name='note'),
    
    url(r'^addnote/$', 'notes.views.add_note', name='add_note'),

    url(r'^changenote/(?P<note_id>\d+)/$', 'notes.views.change_note', name='change_note'),


<<<<<<< HEAD
	url(r'^del_note/(?P<note_id>\d+)/$', 'notes.views.del_note', name='del_note'),

	url(r'^success_delete/(?P<note_id>\d+)/$', 'notes.views.del_note', name='del_note'),



=======
>>>>>>> 8f8032d29f487ace3c84acd0e2454acb5d36e0d5
    url(r'^page/(\d+)/$', 'notes.views.index'),

    
    # ex: /polls/5/results/
  #  url(r'^(?P<note_id>\d+)/results/$', 'notes.views.results', name='results'),
    # ex: /polls/5/vote/
 
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
   
)