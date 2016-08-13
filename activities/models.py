from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Activities(models.Model):

    activities_code = models.CharField(max_length = 64,default=uuid.uuid4)
    country = models.CharField(max_length = 20, blank = False, null = False)
    year = models.CharField(max_length = 10, blank = False, null = False)
    thopic = models.CharField(max_length = 200, blank = False, null = False)
    active = models.BooleanField(default = True)
    isPaid = models.BooleanField(default = False)# to know if the activity as a price
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='activity_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'activity_updater')
    fk_activities_type_code = models.CharField(max_length = 64, blank = False,null = False)

    def __unicode__(self):
        return self.thopic


class signUpActivities(models.Model):

    sign_up_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_activities_code = models.CharField(max_length = 64)
    fk_user = models.ForeignKey(User)

    def __unicode__(self):
        return self.fk_user.username


class ActivitiesType(models.Model):

    activities_type_Code = models.CharField(max_length = 64,default = uuid.uuid4)
    description = models.CharField(max_length = 30, blank = False)
    active = models.BooleanField(default = True, blank = False)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='activities_type_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User,null = True, blank = False ,related_name = "activities_type_modified")


    def __unicode__(self):

        return self.description
