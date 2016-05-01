from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Topic(models.Model):

    topic_code = models.CharField(max_length = 64, default = uuid.uuid4)
    topic_name = models.CharField(max_length = 40, blank = True, null = True)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='topic_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'topic_updater')
    fk_user_professor = models.ForeignKey(User, null = True,blank = True, related_name = 'professor')
    fk_congress = models.CharField(max_length = 64)
    fk_room = models.CharField(max_length = 64, null = True, blank = False)

    def __unicode__(self):
        return self.room_name

"""class Professor(Model.models):

    professor_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='professor_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'professor_updater')
    fk_user_professor = models.ForeignKey(User, null = True,blank = True, related_name = 'professor_user')

    def __unicode__(self):
        return self.professor_code"""