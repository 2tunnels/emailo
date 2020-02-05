import click


@click.group()
def app():
    pass


@app.command()
def parse():
    """Parse given file for emails."""

    click.echo("Hello, world!")
