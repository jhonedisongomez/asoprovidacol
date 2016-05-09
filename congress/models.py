from __future__ import unicode_literals
from django.db import models
import uuid
from django.contrib.auth.models import User

class Congress(models.Model):

    congress_code = models.CharField(max_length = 64,default=uuid.uuid4)
    country = models.CharField(max_length = 20, blank = False, null = False)
    year = models.CharField(max_length = 10, blank = False, null = False)
    thopic = models.CharField(max_length = 200, blank = False, null = False)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='congress_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'congress_updater')

    def __unicode__(self):
        return self.year


class signUpCongress(models.Model):

    sign_up_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_congress_code = models.CharField(max_length = 64)
    fk_user = models.ForeignKey(User)

    def __unicode__(self):
        return self.fk_user.username
