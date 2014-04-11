from django.conf.urls import url

from timeline import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/(?P<search_query>\w+)/$', views.search, name='search'),
]