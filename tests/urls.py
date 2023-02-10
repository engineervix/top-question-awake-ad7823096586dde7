from django.conf.urls import include
from django.urls import path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls


urlpatterns = [
    path("admin/", include(wagtailadmin_urls)),
    path("", include(wagtail_urls)),
]
