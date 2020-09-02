Bulma Widget
============

Bulma widget is a django package that intergrates the Bulma css framework with django forms.


Dependencies
--------------
* Bulma css Framework 0.8.0+

* Django 2.2+


Install
--------------

```
pip install django-bulma-widget
```

Forms
------------

1. Add ```bulma_widget``` to INSTALLED_APPS

2. Modify the fields in your forms by adding the bulma widgets, an example:
   
   ```
   from bulma_widget import widgets
   
   class User(forms.ModelForm):
   
	   username = forms.Charfield(max_length=10, widget=widgets.BulmaTextInput)
	   
	   password = forms.CharField(widget=widgets.BulmaPasswordInput)
   ```


3. Include the ```form.djhtml``` into your templates when you need to render a form.
   
   ```
   {% include 'bulma_widget/form.djhtml' with form=form %}
   ```
![signin screenshot](screenshot/signin.png)




Error Messages
---------------

Form error messages can be included as well, they are included at the top of the form.
```
{% include 'bulma_widget/_form_errors.djhtml' with form=form %}
```



Django Messages
----------------
Django messages can also be included as well

```
{% include 'bulma_widget/_messages.djhtml' %}
```
