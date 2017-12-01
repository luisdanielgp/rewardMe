from django.conf.urls import url, include
from .views import categories, donation
# from modules.organizations.views import organization_details

urlpatterns = [
    # url(r'^categories/(?P<slug>[-\w]+)/$', categories_by_goal, name="categories_list"),
    # url(r'^organizations', include('modules.organizations.urls', namespace="organizations")),
    # url(r'^organizations/(?P<slug>[-\w]+)/$', organization_details, name='organization_details'),
    url(r'^donations/(?P<id>[0-9a-f-]+)/$', categories, name='categories'),
    # url(r'^donations/(?P<goal_id>[0-9a-f-]+)/(?P<cat_id>[0-9a-f-]+)/$',
    #     amount_selection, name='amount_selection'),
    url(r'^donations/(?P<id>[0-9a-f-]+)/(?P<slug>[-\w]+)/$',
        donation, name='amount_selection'),
    url(r'^donations/(?P<id>[0-9a-f-]+)/(?P<slug>[-\w]+)/thanks/$', donation, name='thanks')
]

# e709308b-7f60-41c0-b9c1-c86f57df16c8
