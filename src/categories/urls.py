from django.conf.urls import url
from categories.views import category_list, category_detail

urlpatterns = [
    url(r'^$', category_list, name='category_list'),
    url(r'^(?P<pk>\S+)/$', category_detail, name='category_detail'),
]