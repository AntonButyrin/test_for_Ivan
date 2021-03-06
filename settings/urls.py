from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

# from django.contrib.sitemaps.views import sitemap

# from applications.core.sitemap import (SitemapWeekly, SitemapDaily)
# sitemaps = {'weekly': SitemapWeekly, 'daily': SitemapDaily}


urlpatterns = [
    # path(
    #     'sitemap.xml/',
    #     sitemap,
    #     {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'
    # ),

    path(
        'admin/',
        admin.site.urls,

    ),
    path(
        '',
        include(('applications.main.urls', 'main'), namespace='main'),
    ),
    path(r'^ckeditor/',
         include('ckeditor_uploader.urls')
    ),
]


urlpatterns += staticfiles_urlpatterns() + \
               static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
