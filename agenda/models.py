from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Agenda(models.Model):

    agenda_code = models.CharField(max_length = 64, default = uuid.uuid4)
    schedule = models.CharField(max_length = 20, blank = False, null = False)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='agenda_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'agenda_updater')

    def __unicode__(self):
        return self.schedule

class SignUpSchedule(models.Model):

    sign_up_schedule_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='sign_up_schedule_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'sign_up_schedule_updater')
    fk_professor_activity = models.CharField(max_length = 64)
    fk_agenda = models.CharField(max_length = 64)
