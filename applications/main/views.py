from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import render

from .models import Page


class IndexView(TemplateView):
    template_name = 'index.html'


class PageView(View):

    def get(self, request, page_slug, **kwargs):
        if page_slug:
            model = Page.objects.get(slug=page_slug)
            context = {'model': model}
            template_name = 'Page.html'
            return render(request, template_name, context)
        return HttpResponse(f'Ошибка ')


class PageViewAMP(View):

    def get(self, request, page_slug, **kwargs):
        if page_slug:
            model = Page.objects.get(slug=page_slug)
            context = {'model': model}
            template_name = 'Page.amp.html'
            return render(request, template_name, context)
        return HttpResponse(f'Ошибка ')


class PageViewYA(View):

    def get(self, request, page_slug, **kwargs):
        if page_slug:
            model = Page.objects.get(slug=page_slug)
            context = {'model': model}
            template_name = 'Page.ya.html'
            return render(request, template_name, context)
        return HttpResponse(f'Ошибка ')
