from django import forms
from django.utils.safestring import mark_safe


class BulmaTextInput(forms.widgets.TextInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "input"}
        super().__init__(attrs, *args, **kwargs)


class BulmaNumberInput(forms.widgets.NumberInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "input"}
        super().__init__(attrs, *args, **kwargs)


class BulmaPasswordInput(forms.widgets.PasswordInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "input"}
        super().__init__(attrs, *args, **kwargs)


class BulmaEmailInput(forms.widgets.EmailInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "input"}
        super().__init__(attrs, *args, **kwargs)


class BulmaSelect(forms.widgets.Select):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(
            u"""<div class="select">{}</div>""".format(
                super().render(name, value, attrs)
            )
        )


class BulmaMultiSelect(forms.widgets.SelectMultiple):
    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(
            u"""<div class="select is-multiple">{}</div>""".format(
                super().render(name, value, attrs)
            )
        )


class BulmaFileInput(forms.widgets.ClearableFileInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "file-input"}
        super().__init__(attrs, *args, **kwargs)

    def render(self, name, value, attrs=None):
        return mark_safe(
            u"""<div class="file has-name"><label class="file-label">{}<span class="file-cta"><span class="file-icon">
        <i class="fas fa-upload"></i>
      </span>
      <span class="file-label">
        Choose a file…
      </span></span><span class="file-name" id="filename">No file selected</span></label></div>""".format(
                super().render(name, value, attrs)
            )
        )


class BulmaDateInput(forms.widgets.DateInput):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "portfolio_date input", "type": "date"}
        super().__init__(attrs, *args, **kwargs)


class BulmaTextarea(forms.widgets.Textarea):
    def __init__(self, attrs=None, *args, **kwargs):
        attrs = {"class": "textarea", "maxlength": "255"}
        super().__init__(attrs, *args, **kwargs)
