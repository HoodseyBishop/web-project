from django.conf.urls import url
from questions.views import question_list, question_detail

urlpatterns = [
    url(r'^$', question_list, name='question_list'),
    url(r'^(?P<pk>\d+)/', question_detail, name='question_detail'),
]