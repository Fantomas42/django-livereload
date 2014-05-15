=================
Django-livereload
=================

Application performing a `LiveReload`_ with `tiny-lr`_ once the development
server has started.

Why this project ?
------------------

Recently I started to use `Gulp`_ and `LiveReload`_ to automatize some
tasks. Once an HTML, CSS or JS has changed, a livereload is performed in
the browser to reflect the changes, and I was pretty happy.

But I found one limitation, I cannot perform a livereload of the current
page when I edit Python files, because the development server provided by
Django is not necessary ready when the livereload request is emitted.

That's why I created this application.

Installation
------------

* First install the package on your system: ::

  $ pip install django-livereload

* Then register the ``'livereload'`` application in your ``INSTALLED_APPS``
  setting, after the ``'django.contrib.staticfiles'`` application if used.

Usage
-----

If the livereload server provided by `tiny-lr` is launched (via `Gulp`_,
`Grunt`_ or whatever), the ``runserver`` command will do a livereload on
your browser when the Django development server is ready.

.. _`LiveReload`: http://livereload.com/
.. _`tiny-lr`: https://github.com/mklabs/tiny-lr
.. _`Gulp`: http://gulpjs.com/
.. _`Grunt`: http://gruntjs.com/
