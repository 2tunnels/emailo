from click.testing import CliRunner

from emailo.console import app

runner = CliRunner()


def test_parse_missing_argument() -> None:
    result = runner.invoke(app, ["parse"])

    assert result.exit_code == 2
    assert (
        result.output
        == """Usage: app parse [OPTIONS] FILE
Try "app parse --help" for help.

Error: Missing argument "FILE".
"""
    )


def test_parse() -> None:
    with runner.isolated_filesystem():
        with open("dump.txt", mode="w", encoding="utf-8") as f:
            f.write("Hello john@example.com world!")
            f.write("Hello bill@example.com world!")

        result = runner.invoke(app, ["parse", "dump.txt"])

        assert result.exit_code == 0
        assert result.output == "john@example.com\nbill@example.com\n"


def test_parse_endswith() -> None:
    with runner.isolated_filesystem():
        with open("dump.txt", mode="w", encoding="utf-8") as f:
            f.write("Hello john@gmail.com world!")
            f.write("Hello bill@hotmail.com world!")

        result = runner.invoke(app, ["parse", "dump.txt", "--endswith", "@gmail.com"])

        assert result.exit_code == 0
        assert result.output == "john@gmail.com\n"
