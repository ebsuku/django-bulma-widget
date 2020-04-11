======
Bulma Widget
=======

Bulma widget is a django package that intergrates the Bulma css framework with django forms.


Dependencies
--------------
* Bulma css Framework 0.8.0+

* Django 2.2+


Quick Start
------------

1. Add "bulma_widget" to INSTALLED_APPS

2. Include the 'bulma_widget/form.djhtml' into your templates when you need to render a form.
   ```
   {% include 'bulma_widget/form.djhtml' with form=form %}
   ```


Screenshot
-----------
.. image screenshot/signin.png
