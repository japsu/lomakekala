# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **opts):
        from django.contrib.auth.models import User
        from lomakekala.models import Form, Handler, HandlerType, MailHandler, MailHandlerRecipient

        user, created = User.objects.get_or_create(username='mahti', defaults=dict(
            is_superuser=True,
            is_staff=True
        ))

        if created:
            user.set_password('mahti')
            user.save()

        save_handler = Handler.objects.get(slug='save')
        form, created = Form.objects.get_or_create(slug='test', defaults=dict(
            name='Test form',
            description='This is a test form.',
            code='lomakekala_test_app.forms:TestForm',
        ))

        for name, slug, code in [
            (u'Decide if email should be sent', 'should-send-email', 'lomakekala_test_app.handlers:should_send_email'),
        ]:
            handler_type, unused = HandlerType.objects.get_or_create(
                slug=slug,
                defaults=dict(
                    name=name,
                    code=code,
                ),
            )

            handler, unused = Handler.objects.get_or_create(
                handler_type=handler_type,
                defaults=dict(
                    name=handler_type.name,
                    slug=handler_type.slug,
                )
            )

        mail_handler_type = HandlerType.objects.get(slug='mail-sync')
        mail_handler, unused = Handler.objects.get_or_create(
            slug='mail-test',
            defaults=dict(
                name='Mail test',
                handler_type=mail_handler_type,
            )
        )

        mail_mail_handler, unused = MailHandler.objects.get_or_create(
            handler=mail_handler,
            defaults=dict(
                body_template=u'This is a test with foo={{foo}}.',
                subject_template=u'Test',
            ),
        )

        MailHandlerRecipient.objects.get_or_create(
            mail_handler=mail_mail_handler,
            email_address='japsu+lomakekala@japsu.fi',
            defaults=dict(
                display_name=u'Santtu Pajukanta',
            ),
        )

        should_send_email = Handler.objects.get(slug='should-send-email')

        created = True
        if created:
            form.set_handlers([save_handler, should_send_email, mail_handler])

