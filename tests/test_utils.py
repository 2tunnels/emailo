from emailo.utils import parse_emails


def test_parse_emails_empty() -> None:
    assert parse_emails("Hello, world!") == []


def test_parse_emails_invalid() -> None:
    assert parse_emails("john.@example.com") == []


def test_parse_emails_single() -> None:
    assert parse_emails("john@example.com") == ["john@example.com"]


def test_parse_emails_multiple() -> None:
    assert parse_emails("john@example.com bill@example.com") == [
        "john@example.com",
        "bill@example.com",
    ]


def test_parse_email_sentence_single() -> None:
    assert parse_emails("Hello john@example.com! How are you?") == ["john@example.com"]


def test_parse_email_sentence_multiple() -> None:
    assert parse_emails(
        "Hello john@example.com! How are you? It's bill@example.com!"
    ) == ["john@example.com", "bill@example.com"]


def test_parse_email_sql() -> None:
    assert parse_emails(
        "1:john@example.com:john:pass:John Doe:::1900-00-00:00:M:66:729:67793"
    ) == ["john@example.com"]
