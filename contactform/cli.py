"""Console script for contactform."""

import sys

import click

from .version import __version__, __timestamp__
header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"


@click.command("contactform")
@click.version_option(message=header)
@click.option("-d", "--debug", is_flag=True, help="debug mode")
def cli(debug):

    def exception_handler(
        exception_type, exception, traceback, debug_hook=sys.excepthook
    ):

        if debug:
            debug_hook(exception_type, exception, traceback)
        else:
            click.echo(f"{exception_type.__name__}: {exception}", err=True)

    sys.excepthook = exception_handler

    """cli for contactform."""
    raise RuntimeError("Add application code to contactform/cli.py")
    return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
