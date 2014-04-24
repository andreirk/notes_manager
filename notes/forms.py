# -*- coding: utf-8 -*-
from django import forms

from .models import Note

class NoteAddForm(forms.ModelForm):
	""""""
	class Meta:
		model = Note
		exclude = ['pub_date','change_date', 'author']
		widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
		#fields = ['title','content','category', 'is_published', 'is_chosen']
		labels = {'title' : 'Название',
				  'content': "Текст заметки",
				  'category': "Категория",
				  'is_published':"Опубликовать",
				  'is_chosen': "Отметить как избранная"}


class NoteChangeForm(forms.ModelForm):
	""""""
	class Meta:
		model = Note
		exclude = ['pub_date','change_date', 'author']
		widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }
		#fields = ['title','content','category', 'is_published', 'is_chosen']
		labels = {'title' : 'Название',
				  'content': "Текст заметки",
				  'category': "Категория",
				  'is_published':"Опубликовать",
				  'is_chosen': "Отметить как избранная"}