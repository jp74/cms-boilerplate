[![Build Status](https://drone.io/github.com/jp74/cms-boilerplate/status.png)](https://drone.io/github.com/jp74/cms-boilerplate/latest)

Django Boilerplate for Django 1.6 with Django CMS 3.0
=================================

### Usage
This assumes you have pip and django installed (if not, try `$ sudo easy_install pip`)

	$ django-admin.py startproject --template http://github.com/jp74/cms-boilerplate/zipball/master project_name
	$ cd project_name
	$ pip install -r requirements.txt
	$ python manage.py syncdb --migrate
	$ cd config; ln -s environments/production/settings_local.py settings_local.py

### Settings
Django settings are configured in `config/settings_common.py` and any settings added in `config/settings_local.py` will be picked up and override any previously defined settings.

### Preinstalled Apps
 * [django-cms](https://www.django-cms.org/en/): The easy-to-use and developer-friendly CMS.
 * [South](http://south.aeracode.org/): Intelligent database migrations.
 * [django-compressor](https://github.com/jezdez/django_compressor): Compresses linked and inline javascript or CSS into a single cached file.
 * [easy-thumbnails](http://easy-thumbnails.readthedocs.org/en/latest/usage/): Image resize and cropping library.
 * [django-filer](https://github.com/stefanfoulis/django-filer): File and Image Management Application for django
 * [cmsplugin-filer](https://github.com/stefanfoulis/cmsplugin-filer): django-filer cms plugins for django-cms
 * [django-axes](https://github.com/django-security/django-axes): Keep track of failed login attempts in Django-powered sites.
 * [django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar): A configurable set of panels that display various debug information about the current request/response.
 * [django-reversion](https://github.com/etianen/django-reversion): An extension to the Django web framework that provides comprehensive version control facilities.
 * [django-model-utils](https://github.com/carljm/django-model-utils): Django model mixins and utilities.
 * [django-braces](https://github.com/brack3t/django-braces): Reusable, generic mixins for Django.

### Image compression (easy thumbnails)
http://easy-thumbnails.readthedocs.org/en/2.0.1/ref/optimize/
Install jpegoptim & optipng and add the following to your settings file:

```python
INSTALLED_APP = (
    ...
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    ...
)

THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/usr/bin/jpegoptim {filename}'
}
```

### Credits
https://github.com/nathanwalsh/django-boilerplate
https://github.com/martinogden/django-boilerplate/
http://blog.zacharyvoase.com/2010/02/03/django-project-conventions/
