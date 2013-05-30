from django.conf.urls import patterns, include, url
from shortenerapp.views import index


urlpatterns = patterns('',
   
   #url(r'^$', view=hello_view, name='hello_page'),
   url(r'^$', view=index, name='index_page'),
)
