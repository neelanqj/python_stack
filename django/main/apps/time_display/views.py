# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django.utils import formats

# Create your views here.
def index(request):
	currentDate = datetime.now()
	formattedDate = DateFormat(currentDate)
	context = {
        "time" : currentDate.strftime("%I:%M %p"),
		"date" : formattedDate.format(get_format('DATE_FORMAT'))
    }
	return render(request, "time_display/index.html", context)