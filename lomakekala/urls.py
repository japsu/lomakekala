from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import FormView, IndexView, ThanksView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='lomakekala_index_view'),
    url(r'^(?P<form_slug>[a-z0-9-]+)/?$', FormView.as_view(), name='lomakekala_form_view'),
    url(r'^thanks/?$', ThanksView.as_view(), name='lomakekala_thanks_view'),
)
