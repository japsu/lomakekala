from django.core.mail import EmailMessage
from django.template import Template, Context


def save_model_form(model_form, form_descriptor, handler):
    model_form.save()


def send_mail_sync(form, form_descriptor, handler):
    mail_handler = handler.mail_handler

    context = Context(dict(
        form.cleaned_data,
        form=form,
        form_descriptor=form_descriptor,
        handler=handler,
    ))

    EmailMessage(
        subject=Template(mail_handler.subject_template).render(context),
        body=Template(mail_handler.body_template).render(context),
        from_email=mail_handler.from_address if mail_handler.from_address else settings.DEFAULT_FROM_EMAIL,
        to=mail_handler.get_addresses('to'),
        bcc=mail_handler.get_addresses('bcc'),
        cc=mail_handler.get_addresses('cc'),
    ).send(fail_silently=True)
