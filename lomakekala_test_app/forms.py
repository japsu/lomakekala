# encoding: utf-8

from django import forms

from crispy_forms.layout import Submit, Layout

from lomakekala.utils import horizontal_form_helper, indented_without_label

from .models import TestFormModel


class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.helper = horizontal_form_helper()
        self.helper.layout = Layout(
            'foo',
            indented_without_label(
                Submit('submit', u'Lähetä', css_class='btn-success')
            )
        )

    class Meta:
        model = TestFormModel
