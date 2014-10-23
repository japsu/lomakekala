# encoding: utf-8

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from .models import Form
from .utils import get_code


class FormView(View):
    http_method_names = ['get', 'post']

    def get(self, request, form_slug):
        form_descriptor = get_object_or_404(Form, slug=form_slug)
        form = form_descriptor.initialize_form(request)
        return render(request, 'lomakekala_form_view.jade', dict(form=form))

    def post(self, request, form_slug):
        form_descriptor = get_object_or_404(Form, slug=form_slug)
        form = form_descriptor.initialize_form(request)

        if form.is_valid():
            form_descriptor.handle_valid_form(form)
            return redirect('lomakekala_thanks_view')

        else:
            messages.error(request, u'Ole hyvä ja tarkista lomake.')
            return render(request, 'lomakekala_form_view.jade', dict(form=form))


class IndexView(TemplateView):
    template_name = 'lomakekala_index_view.jade'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(forms=Form.objects.all())
        return context


class ThanksView(TemplateView):
    template_name = 'lomakekala_thanks_view.jade'
