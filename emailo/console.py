from collections import Counter

import click

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
                click.echo(email)

    click.echo("Hello, world!")


@app.command()
@click.argument("file", type=click.Path(exists=True))
def domains(file: str) -> None:
    counter: Counter = Counter()
    max_domain_length = 0

    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            domain = line.strip().split("@")[1]
            domain_length = len(domain)

            if domain_length > max_domain_length:
                max_domain_length = domain_length

            counter[domain] += 1

    for domain, count in sorted(
        counter.items(), key=lambda items: items[1], reverse=True
    ):
        formatted_domain = domain.ljust(max_domain_length)
        click.echo(f"{formatted_domain} {count}")
