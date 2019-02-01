# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect, render
from django.contrib import messages

import re, bcrypt

# Create your views here.
def index(request):
	return redirect('/main')
	
def gateway(request):
	return render(request, 'wishlist/gateway.html')
	
def login(request):
	print "got here!"
	user = User.objects.get(name = request.POST['username'])
	hashed_password = user.password
	entered_password = request.POST['password']
	
	if bcrypt.checkpw(entered_password.encode(), hashed_password.encode()):
		request.session['id'] = user.id
		return redirect('/dashboard')
	else:		
		messages.add_message(request, messages.INFO, 'Invalid username or password. Please try again.')
		return redirect('/main')

def logout(request):
	del request.session['id']
	request.session.modified = True
	
	return redirect('/main')
		
def register(request):
	name = request.POST['name']
	username = request.POST['username']
	datehired = request.POST['datehired']
	password = request.POST['password']	
	confirm_password = request.POST['confirm_password']	
	
	errors = 0

	if not re.match(r"^[a-zA-Z]+$", name):
		messages.add_message(request, messages.INFO, "Invalid name.")
		errors += 1
	
	if len(name) < 3:
		messages.add_message(request, messages.INFO, "Name should be larger than 3 characters.")
		errors += 1
		
	if len(username) < 3:
		messages.add_message(request, messages.INFO, "Username should be larger than 3 characters.")
		errors += 1
		
	if password == "":
		messages.add_message(request, messages.INFO, "Password is not allowed to be empty.")
		errors += 1
	
	if len(password) < 8:
		messages.add_message(request, messages.INFO, "Password is too short.")
		errors += 1
	
	if password != confirm_password:
		messages.add_message(request, messages.INFO, "Passwords do not match.")
		errors += 1
	
	hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
	
	if errors == 0:
		messages.add_message(request, messages.INFO, "Registration Successful! Please Log In.")
		User.objects.create(name=name, username=username, password=hashed_password, datehired=datehired)
		user = User.objects.get(username = username)
		request.session['id'] = user.id
		return redirect('/dashboard')
	else:
		return redirect('/')
	