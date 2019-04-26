# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class alogoEmailRecipients(models.Model):
    name = models.CharField(null=False, blank=True, max_length=200, unique=True)
    email = models.EmailField()
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "alogotech"
        db_table = "alogotech_subscribe"

    def __str__(self):
        return self.email