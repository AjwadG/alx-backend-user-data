#!/usr/bin/env python3
"""
Filtered Logger
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record by filtering the message.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with filtered fields.
        """
        original_message = super().format(record)
        filtered_message = filter_datum(self._fields, self.REDACTION,
                                        original_message, self.SEPARATOR)
        return filtered_message


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
