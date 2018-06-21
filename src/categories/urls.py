from django.conf.urls import url
from categories import views

urlpatterns = [
    url(r'^$', views.CategoryList.as_view(), name='category_list'),
    url(r'^(?P<pk>\S+)/$', views.category_detail, name='category_detail'),
]