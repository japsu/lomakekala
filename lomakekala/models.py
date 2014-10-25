from django.db import models

from .utils import get_code


class HandlerType(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63, unique=True)
    code = models.CharField(max_length=255)

    def handle_valid_form(self, form, form_descriptor, handler):
        handle_func = get_code(self.code)
        return handle_func(form, form_descriptor, handler)

    def __unicode__(self):
        return self.name


class Handler(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63, unique=True)
    handler_type = models.ForeignKey(HandlerType)

    def __unicode__(self):
        return self.name

    def handle_valid_form(self, form, form_descriptor):
        return self.handler_type.handle_valid_form(form, form_descriptor, self)


class MailHandler(models.Model):
    handler = models.OneToOneField(Handler)
    from_address = models.CharField(max_length=255, blank=True)
    subject_template = models.CharField(max_length=1023)
    body_template = models.TextField()

    def get_addresses(self, recipient_type=None):
        query = dict()

        if recipient_type is not None:
            query.update(recipient_type=recipient_type)

        recipients = MailHandlerRecipient.objects.filter(**query)

        return [r.name_and_email for r in recipients]

    def set_recipients(self, recipient_type, names_and_emails):
        self.mailhandlerrecipient_set.filter(recipient_type=recipient_type).delete()

        for display_name, email_address in names_and_emails:
            self.mailhandlerrecipient_set.create(
                display_name=display_name,
                email_address=email_address,
                recipient_type=recipient_type,
            )


RECIPIENT_TYPE_CHOICES = (('to', 'To'), ('cc', 'CC'), ('bcc', 'BCC'))


class MailHandlerRecipient(models.Model):
    mail_handler = models.ForeignKey(MailHandler)
    display_name = models.CharField(max_length=255, blank=True)
    email_address = models.CharField(max_length=255)
    recipient_type = models.CharField(max_length=3, choices=RECIPIENT_TYPE_CHOICES, default='to')

    def __unicode__(self):
        return self.email_address

    @property
    def name_and_email(self):
        if self.display_name:
            return u'{self.display_name} <{self.email_address}>'.format(self=self)
        else:
            return self.email_address


class Form(models.Model):
    name = models.CharField(max_length=63)
    slug = models.CharField(max_length=63, unique=True)
    code = models.CharField(max_length=255)
    is_public = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def initialize_form(self, request, *args, **kwargs):
        FormClass = get_code(self.code)

        if request.method == 'POST':
            return FormClass(request.POST, *args, **kwargs)
        else:
            return FormClass(*args, **kwargs)

    def handle_valid_form(self, form):
        for handler in self.handlers:
            result = handler.handle_valid_form(form, self)
            if result is False:
                break

    @property
    def handlers(self):
        return [fh.handler for fh in self.formhandler_set.order_by('order')]

    def set_handlers(self, new_handlers):
        self.formhandler_set.all().delete()

        order = 0
        for handler in new_handlers:
            order += 10
            self.formhandler_set.create(handler=handler, order=order)


class FormHandler(models.Model):
    form = models.ForeignKey(Form)
    order = models.IntegerField(default=0)
    handler = models.ForeignKey(Handler)

    class Meta:
        ordering = ('form', 'order')
        index_together = [('form', 'order', 'handler')]
