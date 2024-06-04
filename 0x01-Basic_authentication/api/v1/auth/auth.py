#!/usr/bin/env python3
""" Module of Auth """
from typing import TypeVar
from flask import request
from models.user import User


class Auth():
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """ Require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current user """
        return None
