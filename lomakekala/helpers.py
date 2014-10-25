from .models import HandlerType, Handler, MailHandler


def get_or_create_handler_and_type(name, slug, code):
    handler_type, type_created = HandlerType.objects.get_or_create(
        slug=slug,
        code=code,
        defaults=dict(name=name),
    )

    handler, handler_created = Handler.objects.get_or_create(
        slug=slug,
        handler_type=handler_type,
        defaults=dict(name=handler_type.name)
    )

    return handler, handler_created


def get_or_create_mail_handler(
    slug,
    name,
    subject_template,
    body_template,
    to,
    cc=(),
    bcc=(),
    from_address='',
    handler_type_slug='mail-sync',
):
    handler_type = HandlerType.objects.get(slug=handler_type_slug)

    handler, handler_created = Handler.objects.get_or_create(
        slug=slug,
        handler_type=handler_type,
        defaults=dict(name=name),
    )

    mail_handler, mail_handler_created = MailHandler.objects.get_or_create(
        handler=handler,
        defaults=dict(
            subject_template=subject_template,
            body_template=body_template,
            from_address=from_address,
        )
    )

    if mail_handler_created:
        for recipient_type, recipients in [
            ('to', to),
            ('cc', cc),
            ('bcc', bcc),
        ]:
            mail_handler.set_recipients(recipient_type, recipients)

    return handler, mail_handler_created
