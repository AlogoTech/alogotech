# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib import messages
from django.template.loader import get_template
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.db import models
from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from .email import send_welcome_email
from .models import alogoEmailRecipients

# Create your views here.
def home(request):
        return render(request, 'home.html')

def subscribe(request):
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        name = post_data.get("name", None)

        error_msg = validation_utility.validate_email(email)
        if error_msg:
                messages.error(request, error_msg)
        return HttpResponseRedirect(reverse('alogotech:subscribe'))

