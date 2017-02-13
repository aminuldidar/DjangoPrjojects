from django.shortcuts import render_to_response
from django.template.loader import *
from django.template import *
from django.http import HttpResponse
import datetime
#import mysql.connector
import pymysql.cursors

def book_list(request):
	connection = pymysql.connect(host='localhost',user='didar',password='Sophomore@99',db='bookmanage',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			# Create a new record
			sql = "INSERT INTO `books` (`name`, `owner`, `purchase`) \
			VALUES ('Tukunjil', 'Zafar Iqbal', now())"
			cursor.execute(sql)
			# connection is not autocommit by default. So you must commit to save
			# your changes.
			connection.commit()
		
		with connection.cursor() as cursor:
			# Read a single record
			sql = "SELECT * FROM `books`"
			cursor.execute(sql)
			results = cursor.fetchall()
			"""
			for row in results:
				name = row['name']
				owner = row['owner']
				purchase = row['purchase']
			"""	
			  # Now print fetched result
			  # print ("name = %s,owner = %s,purchase = %s" % (name, owner, purchase))
        
	finally:
		connection.close()
	return render_to_response('book_list.html', {'names': results})

def current_datetime(request):
	"""
	    Use local() function to replace the template variables having same name 
	"""
	current_date = datetime.datetime.now()
	
	return render_to_response('current_datetime.html', locals())

def current_datetime5(request):
	"""
	    Use local() function to replace the template variables having same name 
	"""
	current_date = datetime.datetime.now()
	
	return render_to_response('mytemplate.html', locals())
	
def current_datetime4(request):
	"""
		Use render_to_response() function for shortcut
	"""
	
	now = datetime.datetime.now()

	c={'cur_date' : now}
	
	return render_to_response('mytemplate.html', c)
	
def current_datetime3(request):
	"""
	    For dynamic calling of template file use template loader
		In settings in TEMPLATES, DIRS should be set as list for 
		'C:/Users/aislam/DjangoProjects/templates' 
	"""
	now = datetime.datetime.now()
	t= get_template('mytemplate.html') 
	c=Context({'cur_date' : now})
	html=t.render(c)
	return HttpResponse(html)

def current_datetime2(request):
	""" Make the template file independent then open, read and execute """
	now = datetime.datetime.now()
	fp=open('C:/Users/aislam/DjangoProjects/templates/mytemplate.html')
	t= Template(fp.read())
	fp.close()
	c=Context({'cur_date' : now})
	html=t.render(c)
	return HttpResponse(html)
	
	
def current_datetime1(request):
	""" This is for just basic understanding how template works """
	now = datetime.datetime.now()
	t = "<html><body>It is now {{ cur_date }}.</body></html>"
	tm= Template(t)
	c=Context({'cur_date' : now})
	html=tm.render(c)
	return HttpResponse(html)
	

def hours_ahead(request, offset):
	""" http://127.0.0.1:8000/time/plus/3/ this url should hit """
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
	
def show_profile(request):
	html = "<html><body>Here Your profile will show. This is first profile</body></html>"
	return HttpResponse(html)

def foobar_view(request, template_name, tst):
	#html = "<html><body>Here Your profile will show. This is first profile</body></html>"
	return render_to_response(template_name, {'tst': tst})