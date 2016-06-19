from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):

    page_code = models.CharField(max_length = 64, default = uuid.uuid4)
    title = models.CharField(max_length = 100, blank = False)
    body = models.CharField(max_length = 1000, blank = False)
    logo = models.ImageField(blank = True, null = True)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='page_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'page_updater')

    def __unicode__(self):

        return self.title

class PageImage(models.Model):

    page_image_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='page_image_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'page_image_updater')
    fk_page_code = models.CharField(max_length = 64, blank = False, null = False)

    def __unicode__(self):

        obj_page = Page.objects.filter(page_code = self.page_code, active = True)

        return obj_page[0].title
