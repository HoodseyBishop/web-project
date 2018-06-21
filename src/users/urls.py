from django.conf.urls import url
from django.contrib.auth.decorators import login_required
import users.views as user_views

urlpatterns = [
    url(r'^$', user_views.UserList.as_view(), name='user_list'),
    url(r'^signup/$', user_views.SignUp.as_view(), name='user_signup'),
    url(r'^login/$', user_views.Login.as_view(), name='user_login'),
    url(r'^logout/$', login_required(user_views.Logout.as_view()), name='user_logout'),
    url(r'^(?P<pk>\S+)/edit$', user_views.UserEdit.as_view(), name='user_edit'),
    url(r'^(?P<pk>\S+)/$', user_views.UserDetail.as_view(), name='user_detail'),
]