from django.db.models import Q
from django.shortcuts import render, render_to_response, redirect
#from books.models import Book, AuthorForm, Publisher
#from books.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView
#from books.models import Publisher
#from forms import PublisherForm

def my_profile(request):
	
	return render(request,'index.html')



	
	
	
	
	
	