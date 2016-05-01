from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Project(models.Model):

    project_code = models.CharField(max_length  = 64,default = uuid.uuid4)
    name = models.CharField(max_length = 20, blank = False, null = False)
    description = models.CharField(max_length = 300, blank = False, null = False)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='project_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'project_updater')


    def __unicode__(self):
        return self.name
class ProjectUser(models.Model):

    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='project_user_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'project_user_updater')
    fk_user_exponent = models.ForeignKey(User, null = True,blank = True, related_name = 'project_user_exponent')
    fk_project_code = models.CharField(max_length = 64, null = False,blank = False)

    def __unicode__(self):
        return self.active
