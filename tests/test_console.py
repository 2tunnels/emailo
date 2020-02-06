from click.testing import CliRunner

from emailo.console import app

runner = CliRunner()


def test_parse_missing_file_argument() -> None:
    result = runner.invoke(app, ["parse"])

    assert result.exit_code == 2
    assert result.output == (
        """Usage: app parse [OPTIONS] FILE\n"""
        """Try "app parse --help" for help.\n"""
        """\n"""
        """Error: Missing argument "FILE".\n"""
    )


def test_parse() -> None:
    with runner.isolated_filesystem():
        with open("dump.txt", mode="w", encoding="utf-8") as f:
            f.write("Hello john@example.com world!\n")
            f.write("Hello bill@example.com world!\n")

        result = runner.invoke(app, ["parse", "dump.txt"])

        assert result.exit_code == 0
        assert result.output == "john@example.com\nbill@example.com\n"


def test_parse_endswith() -> None:
    with runner.isolated_filesystem():
        with open("dump.txt", mode="w", encoding="utf-8") as f:
            f.write("Hello john@gmail.com world!\n")
            f.write("Hello bill@hotmail.com world!\n")

        result = runner.invoke(app, ["parse", "dump.txt", "--endswith", "@gmail.com"])

        assert result.exit_code == 0
        assert result.output == "john@gmail.com\n"


def test_domains_missing_file_argument() -> None:
    result = runner.invoke(app, ["domains"])

    assert result.exit_code == 2
    assert result.output == (
        """Usage: app domains [OPTIONS] FILE\n"""
        """Try "app domains --help" for help.\n"""
        """\n"""
        """Error: Missing argument "FILE".\n"""
    )


def test_domains() -> None:
    with runner.isolated_filesystem():
        with open("emails.txt", mode="w", encoding="utf-8") as f:
            f.write("john@gmail.com\n")
            f.write("bill@gmail.com\n")
            f.write("alex@hotmail.com\n")

        result = runner.invoke(app, ["domains", "emails.txt"])

        assert result.exit_code == 0
        assert result.output == "gmail.com   2\nhotmail.com 1\n"


def test_domains_percentage() -> None:
    with runner.isolated_filesystem():
        with open("emails.txt", mode="w", encoding="utf-8") as f:
            f.write("john@gmail.com\n")
            f.write("bill@gmail.com\n")
            f.write("alex@hotmail.com\n")

        result = runner.invoke(app, ["domains", "emails.txt", "--percentage"])

        assert result.exit_code == 0
        assert result.output == "gmail.com   66.67%\nhotmail.com 33.33%\n"
