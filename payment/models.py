from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):

    payment_code = models.CharField(max_length = 64, default = uuid.uuid4)
    price = models.CharField(max_length = 5)
    active = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='Payment_creator')
    modified_at = models.DateTimeField(null = True, blank = True)
    fk_user_modified = models.ForeignKey(User, null = True,blank = True, related_name = 'payment_updater')
    fk_activity_code = models.CharField(max_length = 64)

class PaymentPerson(models.Model):

    payment_person_code = models.CharField(max_length = 64, default = uuid.uuid4)
    created_at = models.DateTimeField(auto_now = True,blank = False)
    fk_user_created = models.ForeignKey(User,related_name ='payment_person_creator')
    fk_payment_code = models.CharField(max_length = 64)
    fk_user_paied = models.ForeignKey(User, null = True,blank = True, related_name = 'payment_buyer')
