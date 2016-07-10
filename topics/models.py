from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User
from rooms.models import Room
from activities.models import Activities

class Topic(models.Model):

    topic_code = models.CharField(max_length = 64, default = uuid.uuid4)
    topic_name = models.CharField(max_length = 40, blank = True, null = True)
    profesor_name = models.CharField(max_length = 100, blank = True, null = True)
    description = models.CharField(max_length = 500, blank = True, null = True)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='topic_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'topic_updater')
    #fk_user_professor = models.ForeignKey(User, null = True,blank = True, related_name = 'professor')

    def __unicode__(self):
        return self.topic_name

class ActivityRoom(models.Model):

    activity_room_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='activity_room_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'activity_room_updater')
    fk_room_code = models.CharField(max_length = 64)
    fk_activity_code = models.CharField(max_length = 64)
    fk_topic_code = models.CharField(max_length = 64)

    def __unicode__(self):

        obj_activity = Activities.objects.filter(activities_code = self.fk_activity_code, active = True)
        if(obj_activity):
            activity = obj_activity[0].thopic

            obj_room = Room.objects.filter(room_code = self.fk_room_code,active = True)
            room_name = obj_room[0].room_name

            obj_topic = Topic.objects.filter(topic_code = self.fk_topic_code,active = True)
            topic_name = obj_topic[0].topic_name
            return activity + " - " + topic_name + " - " + room_name
        else:

            return self.activity_room_code
