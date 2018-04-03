from django.contrib import admin
from django.conf.urls import url, include
from core.views import main_page
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page, name='main'),
    url(r'^categories/', include('categories.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^users/', include('users.urls')),
]