"""Runserver command with livereload"""
import urllib
from optparse import make_option

from django.conf import settings
from django.core.management.color import color_style


if 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    from django.contrib.staticfiles.management.commands.runserver import \
        Command as RunserverCommand
else:
    from django.core.management.commands.runserver import \
        Command as RunserverCommand


class Command(RunserverCommand):
    """
    Command for running the development server with Livereload.
    """
    option_list = RunserverCommand.option_list + (
        make_option('--nolivereload', action='store_false',
                    dest='use_livereload', default=True,
                    help='Tells Django to NOT use Livereload.'),
        make_option('--livereload-port', action='store',
                    dest='livereload_port', default='35729',
                    help='Port where Livereload listen.'),
    )
    help = 'Starts a lightweight Web server for development with Livereload.'

    def message(self, message, verbosity=1, style=None):
        if verbosity:
            if style:
                message = style(message)
            self.stdout.write(message)

    def livereload_request(self, **options):
        """
        Performs the livereload request.
        """
        style = color_style()
        verbosity = int(options['verbosity'])
        host = 'localhost:%s' % options['livereload_port']
        try:
            urllib.urlopen('http://%s/changed?files=.' % host)
            self.message('LiveReload request emitted.\n !!', verbosity)
        except IOError:
            self.message('> LiveReload server unreachable at %s' % host,
                         verbosity, style.HTTP_BAD_REQUEST)

    def get_handler(self, *args, **options):
        """
        Entry point to plug the livereload feature.
        """
        handler = super(Command, self).get_handler(*args, **options)
        self.livereload_request(**options)
        return handler
