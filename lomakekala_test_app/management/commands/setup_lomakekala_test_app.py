# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **opts):
        from django.contrib.auth.models import User
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
            code='lomakekala_test_app.forms:TestForm',
        ))

        if created:
            form.set_handlers([save_handler])

