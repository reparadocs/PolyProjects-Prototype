from django.conf.urls import patterns, url

from listings import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<listing_id>\d+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<listing_id>\d+)/$', views.edit, name='edit'),
    url(r'^editPost/(?P<listing_id>\d+)$', views.editPost, name='editPost'),
    url(r'^create/$', views.create, name='create'),
    url(r'^createlisting/$', views.createlisting, name='createlisting')
)
