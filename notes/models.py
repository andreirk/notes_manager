import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    cat_type = models.CharField(max_length=100)
   
    def __unicode__(self): 
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category)
    is_chosen = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField('date published')
    change_date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):  
        return self.title

    def was_published_recently(self):
    	now = timezone.now()	
        return now - datetime.timedelta(days=1) <= self.pub_date <  now

        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'




