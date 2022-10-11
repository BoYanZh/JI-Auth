__version__ = "0.0.3"

from ji_auth.canvas import get_canvas_token
from ji_auth.joj import get_joj_sid
from typer import Typer, echo, Option
import asyncio
import sys

app = Typer(add_completion=False)


@app.command("joj")
def echo_joj_sid(
    disable_mask: bool = Option(
        False, "--disable-mask", help="Use stdin instead of TTY to input password."
    )
):
    """
    Get the SID from JOJ cookies.
    """
    try:
        res = asyncio.get_event_loop().run_until_complete(get_joj_sid(not disable_mask))
        echo("Here is your SID:", file=sys.stderr)
        echo(res)
    except Exception as e:
        echo("Oops, Something went wrong. Please try again.", file=sys.stderr)
        echo(e, file=sys.stderr)


@app.command("canvas")
def echo_canvas_token(
    disable_mask: bool = Option(
        False, "--disable-mask", help="Use stdin instead of TTY to input password."
    )
):
    """
    Get a newly generated token from Canvas.
    """
    try:
        res = asyncio.get_event_loop().run_until_complete(get_canvas_token(not disable_mask))
        echo("Here is your token:", file=sys.stderr)
        echo(res)
    except Exception as e:
        echo("Oops, Something went wrong. Please try again.", file=sys.stderr)
        echo(e, file=sys.stderr)


if __name__ == "__main__":
    app()
