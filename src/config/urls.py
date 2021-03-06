from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',

    # Admin Url
    # (r'^$', RedirectView.as_view(url='/admin/')),

    # Admin Url
    url(r'^admin/', include(admin.site.urls)),

    # # Auth API
    url(r'^api/1/', include('administration.urls')),

    # API
    # url(r'^api/1/', include('starter_app.urls', namespace='starter-api')),
    url(r'^api/1/', include('paparazzi.urls', namespace='paparazzi-api')),

    # Api docs
    url(r'^docs/', include('rest_framework_swagger.urls')),

    # Index
    # url(r'^', include('starter_app.urls')),
    # url(r'^', include('paparazzi.urls')),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)