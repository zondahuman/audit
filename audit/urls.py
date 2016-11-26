from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from verify import views,record


urlpatterns = patterns('',
    # Examples:
    url(r'^verify/index/', views.index, name='index'),
    url(r'^verify/add/', record.add, name='add'),
    url(r'^verify/insert/', record.insert, name='insert'),
    url(r'^verify/submit/', record.submit, name='submit'),
)
