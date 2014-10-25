# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **opts):
        from django.contrib.auth.models import User
        from lomakekala.helpers import get_or_create_handler_and_type, get_or_create_mail_handler
        from lomakekala.models import Form, Handler

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

        should_send_email, unused = get_or_create_handler_and_type(
            name=u'Decide if email should be sent',
            slug='should-send-email',
            code='lomakekala_test_app.handlers:should_send_email'
        )

        mail_handler, unused = get_or_create_mail_handler(
            name='Mail test',
            slug='mail-test',
            body_template=u'This is a test with foo={{foo}}.',
            subject_template=u'Test',
            to=(('Santtu Pajukanta', 'japsu+lomakekala@japsu.fi'),),
        )

        if created:
            form.set_handlers([save_handler, should_send_email, mail_handler])

