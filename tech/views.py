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
 
def contact(request):
        if request.method == 'POST':
                 name = request.POST.get('name')
                 email = request.POST.get('email')
                 message = request.POST.get('mesage')

                 # email
                 subject = 'contact Form received'
                 from_email= settings.DEFAULT_FROM_EMAIL
                 to_email = [settings.DEFAULT_FROM_EMAIL]

                 context = {
                         'user': name,
                         'email': email,
                         'message': message
                 }
                 contact_message = get_template('contact_message.txt').render(context)
                 send_mail(subject, contact_message, from_email,to_email, fail_silently=True)

                 return render(request, 'home.html', {})

  

       
