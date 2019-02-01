# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	response = "index"
	return HttpResponse(response)
	
def new(request):
	response = "new"
	return HttpResponse(response)
	
def create(request):
	response = "create"
	return redirect('/')
	
def show(request, blog):
	response = "placeholder to display blog " +blog
	
	return HttpResponse(response)
	
def edit(request, blog):
	response = "placeholder"
	return HttpResponse(response)
	
def destroy(request, blog):
	response = "destroy"
	return redirect('/')