=================
Django-livereload
=================

Application performing a `LiveReload`_ with `tiny-lr`_ once the development
server is ready.

Why this project ?
------------------

I recently started using `Gulp`_ and `LiveReload`_ to automatize some
tasks. Everytime an HTML, CSS or JS file changes, a livereload is performed in
the browser to reflect those changes, and I was pretty happy with that.

But I found one limitation, I cannot perform a livereload of the current
page when editing Python files because the development server provided by
Django is not necessary ready as soon as the livereload request is emitted.

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
your browser whenever the Django development server is ready.

.. _`LiveReload`: http://livereload.com/
.. _`tiny-lr`: https://github.com/mklabs/tiny-lr
.. _`Gulp`: http://gulpjs.com/
.. _`Grunt`: http://gruntjs.com/
