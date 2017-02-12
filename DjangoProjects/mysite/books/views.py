from django.db.models import Q
from django.shortcuts import render, render_to_response
from books.models import Book
from books.forms import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import PublisherForm
def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
		Q(title__icontains=query) |
		Q(authors__first_name__icontains=query) |
		Q(authors__last_name__icontains=query)
		)
		#print(qset)
		results = Book.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("books/search.html", {
		"results": results,
		"query": query
		})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			topic = form.cleaned_data['topic']
			message = form.cleaned_data['message']
			sender = form.cleaned_data.get('sender', 'noreply@example.com')
			print(topic, message, sender)
			"""
			t=send_mail(
			'Feedback from your site, topic: %s' % topic,
			message, sender,
			['aminul.didar@gmail.com']
			)
			"""
			#url = reverse('thanks', kwargs={'name': sender})
			#return HttpResponseRedirect(url) #'/contact/thanks?name=aminul'
			
			return HttpResponseRedirect(reverse('ul_name', kwargs={'tst': sender})) 
	else:
		form = ContactForm()
	return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))

def add_publisher(request):
	if request.method == 'POST':
		form = PublisherForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add_publisher/thanks/')
	else:
		form = PublisherForm()
	return render_to_response('books/add_publisher.html', {'form': form})
	
def thanks(request, tst):
	#print("The name is" % str(name))
	#query = request.GET.get('name', '')
	return render_to_response(request,'books/thanks.html',{'tst' : tst})

def click(request):
	#print("The name is" % str(name))
	return render(request,'books/click.html')
	
	
	
	
	
	
	