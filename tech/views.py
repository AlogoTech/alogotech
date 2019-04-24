# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404,HttpResponseRedirect

from django.shortcuts import render,redirect

from .email import send_welcome_email
from .forms import subscriberForm
# Create your views here.

def home(request):
    return render(request, 'home.html')


def alogo_email(request):
    if request.method == 'POST':
        form = subscriberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = alogoEmailRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('alogo_email')
            #.................
    return render(request, 'email/techmail.html', {"Form":form})