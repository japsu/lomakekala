from importlib import import_module


def get_code(path):
    """
    Given "core.utils:get_code", imports the module "core.utils" and returns
    "get_code" from it.
    """
    module_name, member_name = path.split(':')
    module = import_module(module_name)
    return getattr(module, member_name)


def make_horizontal_form_helper(helper):
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-3'
    helper.field_class = 'col-md-9'
    return helper


def horizontal_form_helper():
    from crispy_forms.helper import FormHelper
    return make_horizontal_form_helper(FormHelper())


def indented_without_label(input, css_class='col-md-offset-3 col-md-9'):
    from crispy_forms.layout import Div
    return Div(Div(input, css_class='controls {}'.format(css_class)), css_class='form-group')
