"""Setup script of django-livereload"""
from setuptools import setup
from setuptools import find_packages

import livereload

setup(
    name='django-livereload',
    version=livereload.__version__,

    description='LiveReload with the Django development server',
    long_description=open('README.rst').read(),

    keywords='django, server, runserver, livereload',

    author=livereload.__author__,
    author_email=livereload.__email__,
    url=livereload.__url__,

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],

    license=livereload.__license__,
    include_package_data=True,
    install_requires=['beautifulsoup4>=4.3.2'],
)
