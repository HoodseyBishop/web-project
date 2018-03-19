from django.conf.urls import url
from users.views import user_list, user_detail, user_signup, user_login

urlpatterns = [
    url(r'^$', user_list, name='user_list'),
    url(r'^signup/$', user_signup, name='user_signup'),
    url(r'^login/$', user_login, name='user_login'),
    url(r'^(?P<pk>\S+)/$', user_detail, name='user_detail'),
]