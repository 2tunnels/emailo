import click


@click.group()
def app() -> None:
    pass


@app.command()
def parse() -> None:
    """Parse given file for emails."""

    click.echo("Hello, world!")
