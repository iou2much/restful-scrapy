from django.conf.urls import patterns, url

urlpatterns = patterns('spider.views',
    url(r'^api/feed/$', 'feed'),
)
