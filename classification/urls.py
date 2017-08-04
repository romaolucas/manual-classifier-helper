from django.conf.url import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'/review/(?P<tweets_to_review>[0-9]+)/$', views.review, name='review_tweets'),
]
