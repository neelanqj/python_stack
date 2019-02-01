# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
 
# Create your views here.
def index(request):
	count = request.session['count']
	count = int(count) + 1
	request.session['count'] = count
	word = get_random_string(length=14)
	
	content = {
		"attempt": request.session['count'],
		"randomWord": word
	}
	
	return render(request, "random_word/index.html", content)
