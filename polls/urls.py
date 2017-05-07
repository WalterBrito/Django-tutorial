from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5
    # detail(request=<HttpRequest object>, question_id='34')
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results
    # detail(request=<HttpRequest object>, question_id='34')
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote
    # detail(request=<HttpRequest object>, question_id='34')
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]