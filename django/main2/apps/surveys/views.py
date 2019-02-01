# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
def index(request):
	return render(request, "surveys/index.html")
	
def results(request):
	content = request.session['content']
	return render(request, "surveys/results.html", content)
	
def process(request):
	count = request.session.get('count')
	count = int(count) + 1
	request.session['count'] = count
	
	content = {
		"name" : request.POST['name'],
		"location": request.POST['location'],
		"language": request.POST['language'],
		"comment": request.POST['comment'],
		"pageSubmits": request.session['count']
	}
	request.session['content'] = content
	return redirect("/results")