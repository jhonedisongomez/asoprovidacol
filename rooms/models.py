from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Room(models.Model):

    room_code = models.CharField(max_length = 64, default = uuid.uuid4)
    room_name = models.CharField(max_length = 40, blank = True, null = True)
    town = models.CharField(max_length = 40, blank = True, null = True)
    address = models.CharField(max_length = 40, blank = True, null = True)
    capacity = models.IntegerField(blank = True, null = True)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='room_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'room_updater')


    def __unicode__(self):
        return self.room_name
