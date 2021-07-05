__version__ = "0.0.1"

from ji_auth.canvas import get_canvas_token
from typer import Typer, echo
from ji_auth.joj import get_joj_sid
import asyncio

app = Typer(add_completion=False)


@app.command("joj")
def echo_joj_sid():
    """
    Get the SID from JOJ cookies.
    """
    try:
        res = asyncio.get_event_loop().run_until_complete(get_joj_sid())
        echo("Here is your SID:")
        echo(res)
    except:
        echo("Oops, Something went wrong. Please try again.")


@app.command("canvas")
def echo_canvas_token():
    """
    Get a newly generated token from Canvas.
    """
    try:
        res = asyncio.get_event_loop().run_until_complete(get_canvas_token())
        echo("Here is your token:")
        echo(res)
    except:
        echo("Oops, Something went wrong. Please try again.")


if __name__ == "__main__":
    app()
