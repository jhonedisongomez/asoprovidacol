from __future__ import unicode_literals
import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):

    country_code = models.CharField(max_length = 64,default = uuid.uuid4, null = False, blank = True)
    country_name = models.CharField(max_length = 64, null = False, blank = False)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='country_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'country_updater')

    def __unicode__(self):

        return self.country_name


class section(models.Model):

    section_code = models.CharField(max_length = 64, default = uuid.uuid4, blank = False, null = True)
    section_name = models.CharField(max_length = 30, blank = False, null = False)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='section_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'section_updater')
    fk_country_code = models.CharField(max_length = 64, blank = False, null = True)
    fk_section_code = models.CharField(max_length = 64, blank = True, null = True)
    fk_section_type_code = models.CharField(max_length = 64, blank = False, null = True)


    def __unicode__(self):

        return self.section_name

class sectionType(models.Model):

    section_type_code = models.CharField(max_length = 64, default = uuid.uuid4, blank = False,null = True)
    section_type_name = models.CharField(max_length = 40, blank = False, null = True)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='section_type_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'section_type_updater')

    def __unicode__(self):

        return self.section_type_name
