import re
from typing import List

_email_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")


def parse_emails(string: str) -> List[str]:
    return _email_regex.findall(string)
