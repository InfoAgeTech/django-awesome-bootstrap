* Note: This is still a work in progress.  i will release a 1.x when it's stable.

django-awesome-bootstrap
========================
Twitter Bootstrap + Font Awesome for Django.

* Twitter Bootstrap 3.x: https://github.com/twbs/bootstrap
* Font Awesome 4.x: https://github.com/FortAwesome/Font-Awesome

This is different from `django-twitter-bootstrap <https://github.com/estebistec/django-twitter-bootstrap>`_ in a few ways:

#. This also includes `font-awesome <http://fontawesome.io/>`_
#. The folder structure is setup differently to avoid file naming collisions with static content from different projects

Steven, the owner of the project, did a great job with the documentation for that project.  So much of what you will find below will be similar to, or the same as, what you will find in his project (thanks Steven :)). 

Configuration
=============
Install the app::

    pip install django-awesome-bootstrap

Add the app to your installed apps::

    # settings.py:
    
    INSTALLED_APPS = (
       ...
       'awesome_bootstrap',
       ...
    )

This also assumes you haven't removed ``django.contrib.staticfiles.finders.AppDirectoriesFinder`` from the ``STATICFILES_FINDERS`` config setting.

django-pipeline
===============
`django-pipeline <https://github.com/cyberdelia/django-pipeline>`_ is not required, but highly recommended when dealing with static content.  This project is setup to prevent naming collisions with other static projects.  So when static is collected via::

    python manage.py collectstatic

There will be separate folders for ``twitter_bootstrap`` and for ``font_awesome``.  This way their static file naming convention remain namespaced to their app.  So when adding these statics files into your django-pipeline configuration settings, you can simply do::

   PIPELINE_CSS = {
      'standard': {
        'source_filenames': (
            ...
            'twitter_bootstrap/dist/css/bootstrap.min.css',
            'twitter_bootstrap/dist/css/bootstrap-theme.min.css',
            'font_awesome/css/font-awesome.min.css',
            ...
            # Put your css statics here
        ),
        'output_filename': 'css/YOUR-OUTPUT-FILE_NAME.css',
      }
   }
   
Or you can use individual components from each projects::

   PIPELINE_CSS = {
      'standard': {
        'source_filenames': (
            ...
            'twitter_bootstrap/less/alerts.less',
            'twitter_bootstrap/less/dropdowns.less',
            'font_awesome/less/font-awesome.less',
            ...
            # Put your css statics here               
        ),
        'output_filename': 'css/YOUR-OUTPUT-FILE_NAME.css',
      }
   }
