from django.conf.urls import url

from . import views

app_name = 'classification'
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'/review/(?P<tweets_to_review>[0-9]+)/$', views.review, name='review_tweets'),
]
