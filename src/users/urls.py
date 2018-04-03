from django.conf.urls import url
from django.contrib.auth.decorators import login_required
import users.views as user_views

urlpatterns = [
    url(r'^$', user_views.user_list, name='user_list'),
    url(r'^signup/$', user_views.user_signup, name='user_signup'),
    url(r'^login/$', user_views.Login.as_view(), name='user_login'),
    url(r'^logout/$', login_required(user_views.Logout), name='user_login'),
    url(r'^(?P<pk>\S+)/$', user_views.user_detail, name='user_detail'),
]