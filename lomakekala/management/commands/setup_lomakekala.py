# encoding: utf-8

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **opts):
        from ...models import HandlerType, Handler

        for name, slug, code in [
            (u'Save model form', 'save', 'lomakekala.handlers:save_model_form'),
            (u'Send mail (synchronous)', 'mail-sync', 'lomakekala.handlers:send_mail_sync'),
        ]:
            HandlerType.objects.get_or_create(
                slug=slug,
                defaults=dict(
                    name=name,
                    code=code,
                ),
            )

        save_handler_type = HandlerType.objects.get(slug='save')
        Handler.objects.get_or_create(
            handler_type=save_handler_type,
            defaults=dict(
                name=save_handler_type.name,
                slug=save_handler_type.slug,
            ),
        )
