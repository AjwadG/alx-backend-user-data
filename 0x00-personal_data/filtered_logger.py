#!/usr/bin/env python3
"""
Filtered Logger
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter the given `message` by replacing the values of the fields given in
    `fields` with the `redaction` string. Separate the fields with `separator`.

    Args:
        fields (List[str]): List of field names to filter.
        redaction (str): String to replace the field values with.
        message (str): String to filter.
        separator (str): String used to separate fields in the message.

    Returns:
        str: Filtered message.
    """
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message
