# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def index(request):
	return redirect('/')