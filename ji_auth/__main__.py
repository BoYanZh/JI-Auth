__version__ = "0.0.8"

from ji_auth.canvas import get_canvas_token
from ji_auth.joj import get_joj_sid
from ji_auth.coursesel import get_coursesel_jsid
from typer import Typer, echo, Option, Exit, main
import asyncio
import sys

app = Typer(add_completion=False)


def version_callback(value: bool) -> None:
    if value:
        echo(__version__)
        raise Exit()


def show_version(
    version: bool = Option(
        None, "--version", callback=version_callback, help="Show version."
    ),
) -> None:
    pass


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
        res = asyncio.run(get_joj_sid(not disable_mask))
        echo("Here is your SID:", file=sys.stderr)
        echo(res)
    except Exception as e:
        echo("Oops, Something went wrong. Please try again.", file=sys.stderr)
        echo(e, file=sys.stderr)

@app.command("coursesel")
def echo_coursesel_sid(
    disable_mask: bool = Option(
        False, "--disable-mask", help="Use stdin instead of TTY to input password."
    )
):
    """
    Get the JSESSIONID from JI Coursesel.
    """
    try:
        res = asyncio.run(get_coursesel_jsid(not disable_mask))
        echo("Here is your JSESSIONID:", file=sys.stderr)
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
        res = asyncio.run(
            get_canvas_token(not disable_mask)
        )
        echo("Here is your token:", file=sys.stderr)
        echo(res)
    except Exception as e:
        echo("Oops, Something went wrong. Please try again.", file=sys.stderr)
        echo(e, file=sys.stderr)


app = main.get_group(app)
parameters = main.get_params_from_function(show_version)
(version_param,) = parameters.values()
click_version_param, _ = main.get_click_param(version_param)
app.params.append(click_version_param)


if __name__ == "__main__":
    app()
