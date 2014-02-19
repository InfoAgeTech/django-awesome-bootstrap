.. |version| image:: https://badge.fury.io/py/django-awesome-bootstrap.png
    :target: http://badge.fury.io/py/django-awesome-bootstrap
.. |downloads| image:: https://pypip.in/d/django-awesome-bootstrap/badge.png
    :target: https://crate.io/packages/django-awesome-bootstrap
.. |license| image:: https://pypip.in/license/django-awesome-bootstrap/badge.png
    :target: https://pypi.python.org/pypi/django-awesome-bootstrap/

|version| |downloads| |license|

django-awesome-bootstrap
========================
Twitter Bootstrap + Font Awesome for Django.

* Twitter Bootstrap 3.1.1: https://github.com/twbs/bootstrap
* Font Awesome 4.0.3: https://github.com/FortAwesome/Font-Awesome

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

Contributing/Updating Submodules
================================

Steps to update to the latest version of twitter bootstrap and font awesome submodules (this assumes you're already in the project root):

1. Create a branch from master

2. Update the submodules::

    $ cd awesome_bootstrap/static/twitter_bootstrap
    $ git pull origin
    $ git checkout v3.1.1
    
    $ cd ../font_awesome
    $ git pull origin
    $ git checkout v4.0.3

3. Update the version is the setup.py to coincide with twitter bootstrap's version

4. Update the version in this readme to same version at step #3

Then commit the changes, submit the pull request and you're done!

Versioning
==========

django-awesome-bootstrap will follow a similar version control setup to django-twitter-bootstrap. Versions of this package should match versions of Bootstrap, where available and will take the latest releases to font-awesome with those updates. This presents something of a problem if and when we need to make updates to the packaging here. We can't just upgrade any of the three common components of semantic versioning, because those map to versions of Bootstrap. So, we'll use revisions when needed.

E.g., suppose we have django-awesome-bootstrap 3.0.2 which packages Twitter Bootstrap 3.0.2. If we need to enhance or fix the packaging, we release it as revised version 3.0.2-1.

Therefore, if you're getting a packaging for the first time you could specify it as a very tight range of that target version or no less than the next patch level version. E.g., target 3.0.2 with >=3.0.2,<3.0.3. Each of these captures all revisions to packagings targetting a specific version of Bootstrap.

Finally, it should be re-iterated that the need for this should be the exception and versions should generally mirror Bootstrap more directly going forward.
