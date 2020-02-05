import re
from typing import List

from email_validator import EmailNotValidError, validate_email

_email_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")


def parse_emails(string: str) -> List[str]:
    emails = _email_regex.findall(string)

    valid_emails = []

    for email in emails:
        try:
            valid_email = validate_email(email, check_deliverability=False)["email"]
        except EmailNotValidError:
            continue

        valid_emails.append(valid_email)

    return valid_emails
