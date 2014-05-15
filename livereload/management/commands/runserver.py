"""Runserver command with livereload"""
import urllib

from optparse import make_option
from django.conf import settings

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
                    dest='ivereload_port', default='35729',
                    help='Port where Livereload listen.'),
    )
    help = 'Starts a lightweight Web server for development with Livereload.'

    def livereload_request(self):
        """
        Performs the livereload request.
        """
        host = 'localhost:%s' % self.options.livereload_port
        try:
            urllib.urlopen('http://%s/changed?files=.' % host)
        except IOError:
            pass

    def get_handler(self, *args, **options):
        """
        Entry point to plug the livereload feature.
        """
        handler = super(Command, self).get_handler(*args, **options)
        self.livereload_request()
        return handler
