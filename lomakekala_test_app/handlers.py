def should_send_email(form, form_descriptor, handler):
    return form.cleaned_data['send_email']
