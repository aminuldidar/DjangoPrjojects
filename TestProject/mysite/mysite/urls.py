"""
mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import *
from django.contrib import admin	
from mysite.views import *
from books.views import *
from books.models import *

book_info = {
"queryset" : Book.objects.all().order_by("-publication_date"),
}

urlpatterns = [
	url(r'^$', book_list),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
	url(r'^profile/$', show_profile),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^book_list/$', book_list),
	url(r'^search/$', search),
	url(r'^contact/$', contact),
	url(r'^contact/thanks/(?P<tst>[^/]+)/$', thanks, name='ul_name'),
	url(r'^click/$', click, name='click_me'),
	url(r'^add_publisher/$', add_publisher),
	url(r'^bar/$', foobar_view, {'template_name': 'temp.html', 'tst' : 'test'}),
	#url(r'^books/$', list_detail.object_list, book_info),
	
]