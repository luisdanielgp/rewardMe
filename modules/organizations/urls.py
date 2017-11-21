from django.conf.urls import url
from django.contrib import admin
from .views import organizations, organization_details

urlpatterns = [
    url(r'^organizations/$', organizations, name="organization_list"),
    url(r'^organizations/(?P<slug>[-\w]+)/$', organization_details, name='organization_details'),

]
