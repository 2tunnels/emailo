from collections import Counter
from typing import Optional

import click

from emailo.utils import parse_emails


@click.group()
def app() -> None:
    pass


@app.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--endswith", type=str)
def parse(file: str, endswith: Optional[str]) -> None:
    """Parse given file for emails."""

    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            for email in parse_emails(line):
                if endswith and not email.endswith(endswith):
                    continue

                click.echo(email)


@app.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--percentage", is_flag=True)
def domains(file: str, percentage: bool = False) -> None:
    counter: Counter = Counter()
    max_domain_length = 0
    total = 0

    with open(file, mode="r", encoding="utf-8") as f:
        for line in f:
            domain = line.strip().split("@")[1]
            domain_length = len(domain)

            if domain_length > max_domain_length:
                max_domain_length = domain_length

            counter[domain] += 1
            total += 1

    for domain, count in sorted(
        counter.items(), key=lambda items: items[1], reverse=True
    ):
        formatted_domain = domain.ljust(max_domain_length)

        if percentage:
            p = count / total * 100
            click.echo(f"{formatted_domain} {p:.2f}%")
        else:
            click.echo(f"{formatted_domain} {count}")
