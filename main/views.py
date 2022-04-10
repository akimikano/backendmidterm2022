from django.shortcuts import render
from django.views.generic import TemplateView

from main.models import Post


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context