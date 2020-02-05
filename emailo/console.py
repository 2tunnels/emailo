import click
from email_validator import EmailNotValidError, validate_email

from emailo.utils import parse_emails


@click.group()
def app() -> None:
    pass


@app.command()
@click.argument("file", type=click.Path(exists=True))
def parse(file: str) -> None:
    """Parse given file for emails."""

    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            for email in parse_emails(line):
                try:
                    email = validate_email(email, check_deliverability=False)["email"]
                    click.echo(email)
                except EmailNotValidError:
                    pass

    click.echo("Hello, world!")
