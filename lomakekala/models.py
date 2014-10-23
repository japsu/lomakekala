from django.db import models

from .utils import get_code


class Handler(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63, unique=True)
    code = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    def handle_valid_form(self, form, form_descriptor):
        handler = get_code(self.code)
        handler(form, form_descriptor)


class Form(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63, unique=True)
    code = models.CharField(max_length=255)
    handlers = models.ManyToManyField(Handler, blank=True)

    def __unicode__(self):
        return self.name

    def initialize_form(self, request, *args, **kwargs):
        FormClass = get_code(self.code)

        if request.method == 'POST':
            return FormClass(request.POST, *args, **kwargs)
        else:
            return FormClass(*args, **kwargs)

    def handle_valid_form(self, form):
        for handler in self.handlers.all():
            handler.handle_valid_form(form, self)
