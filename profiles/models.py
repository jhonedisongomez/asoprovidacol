from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User

class IdCard(models.Model):

    id_card_code = models.CharField(max_length = 64, default = uuid.uuid4)
    active = models.BooleanField(default = True)
    is_downloaded = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='id_card_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'id_card_updater')
    fk_sign_activity_code = models.CharField(max_length = 64)
