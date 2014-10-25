# encoding: utf-8

from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from .models import Form
from .utils import get_code


class FormView(View):
    http_method_names = ['get', 'post']

    def get_context_data(self, request, form_slug):
        form_descriptor = get_object_or_404(Form, slug=form_slug)
        form = form_descriptor.initialize_form(request)

        return dict(
            form_descriptor=form_descriptor,
            form=form,
        )

    def get(self, request, form_slug):
        vars = self.get_context_data(request, form_slug)
        return render(request, 'lomakekala_form_view.jade', vars)

    def post(self, request, form_slug):
        vars = self.get_context_data(request, form_slug)
        form = vars['form']
        form_descriptor = vars['form_descriptor']

        if form.is_valid():
            form_descriptor.handle_valid_form(form)
            return redirect('lomakekala_thanks_view', form_slug)

        else:
            messages.error(request, u'Ole hyvä ja tarkista lomake.')
            return render(request, 'lomakekala_form_view.jade', vars)


class IndexView(TemplateView):
    template_name = 'lomakekala_index_view.jade'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(forms=Form.objects.filter(is_public=True))
        return context


class ThanksView(TemplateView):
    template_name = 'lomakekala_thanks_view.jade'

    def get(self, request, form_slug):
        get_object_or_404(Form, slug=form_slug)
        return super(ThanksView, self).get(request)
