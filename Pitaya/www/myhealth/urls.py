from django.conf.urls import url

from . import views

app_name = 'myhealth'
urlpatterns = [
    # ex: /myhealth/
    url(r'^$', views.index, name='index'),
    # ex: /myhealth/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /myhealth/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /myhealth/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
