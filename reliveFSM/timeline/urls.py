from django.conf.urls import url

from timeline import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^search/(?P<search_query>\w+)/$', views.search, name='search'),
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'^test/$', views.test),
    # url(r'^timeline/$', views.timeline),
]