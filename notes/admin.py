from django.contrib import admin

# Register your models here.
from notes.models import Note, Category


		


admin.site.register(Note)

admin.site.register(Category)