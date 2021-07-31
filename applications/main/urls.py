from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.IndexView.as_view(),
        name='index',
    ),
    path(
        '<slug:page_slug>/',
        views.PageView.as_view(),
        name='page_slug',
    ),
    path(
        '<slug:amp>/<slug:page_slug>/',
        views.PageViewAMP.as_view(),
        name='amp',
    ),
    path(
        '<slug:ya>/<slug:page_slug>/',
        views.PageViewYA.as_view(),
        name='ya',
    )
]
