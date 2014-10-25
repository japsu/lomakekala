from django.contrib import admin
from .models import HandlerType, Handler, Form, FormHandler, MailHandler, MailHandlerRecipient


class HandlerTypeAdmin(admin.ModelAdmin):
    model = HandlerType
    list_display = ('slug', 'name', 'code')


class FormHandlerInline(admin.TabularInline):
    model = FormHandler
    extra = 0


class FormAdmin(admin.ModelAdmin):
    model = Form
    inlines = (FormHandlerInline,)
    list_display = ('slug', 'name', 'code')


class MailHandlerRecipientInline(admin.TabularInline):
    model = MailHandlerRecipient
    extra = 0


class MailHandlerAdmin(admin.ModelAdmin):
    model = MailHandler
    inlines = (MailHandlerRecipientInline,)
    list_display = ('handler',)


admin.site.register(HandlerType, HandlerTypeAdmin)
admin.site.register(Handler)
admin.site.register(Form, FormAdmin)
admin.site.register(MailHandler, MailHandlerAdmin)
