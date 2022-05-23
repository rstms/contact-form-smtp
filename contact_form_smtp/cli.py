"""Console script for contactform."""

import sys

import click
import uvicorn

from .settings import DEBUG, HOST, LOG_LEVEL, PORT
from .version import __timestamp__, __version__

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"

log_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


@click.command("contactform")
@click.version_option(message=header)
@click.option("-d", "--debug", is_flag=True, default=DEBUG, help="debug mode")
@click.option("-h", "--host", type=str, default=HOST, help="listen address")
@click.option("-p", "--port", type=int, default=PORT, help="listen port")
@click.option(
    "-l",
    "--log-level",
    default=LOG_LEVEL,
    type=click.Choice(log_levels),
    help=f"log level: {repr(log_levels)}",
)
def cli(debug, host, port, log_level):
    """email sender for a web page contact form"""

    def exception_handler(
        exception_type, exception, traceback, debug_hook=sys.excepthook
    ):

        if debug:
            debug_hook(exception_type, exception, traceback)
        else:
            click.echo(f"{exception_type.__name__}: {exception}", err=True)

    sys.excepthook = exception_handler

    sys.exit(
        uvicorn.run(
            "contact_form_smtp.app:app",
            host=host,
            port=port,
            log_level=log_level.lower(),
        )
    )


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
