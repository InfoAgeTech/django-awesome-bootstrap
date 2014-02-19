from __future__ import unicode_literals

import os

from setuptools import find_packages
from setuptools import setup


classifiers = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
]

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-awesome-bootstrap',
    version='3.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A Django app for including twitter bootstrap and font awesome.',
    long_description=README,
    url='https://github.com/infoagetech/django-awesome-bootstrap',
    download_url='https://pypi.python.org/pypi/django-awesome-bootstrap',
    author='Troy Grosfield',
    maintainer='Troy Grosfield',
    classifiers=classifiers,
)
