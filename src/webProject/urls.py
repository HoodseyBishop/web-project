from django.contrib import admin
from django.conf.urls import url, include
from core.views import main_page
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_page, name='main'),
    url(r'^categories/', include('categories.urls')),
    url(r'^questions/', include('questions.urls')),
    url(r'^users/', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns