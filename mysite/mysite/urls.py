"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from book.views import *
urlpatterns = [
    url(r'^index/$', index),
    url(r'^$', index),
    url(r'^add_book/$', add_book),
    url(r'^delete_book/$', delete_book),
    url(r'^add_author/$', add_author),
    url(r'^updata_book/$', updata_book),
    url(r'^updata_book/do/$', do_updata_book),    
	url(r'^book/$', the_book),    	
	url(r'^search/$', search),    	
]
