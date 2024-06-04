#!/usr/bin/env python3
""" Module of Basic Auth"""
from typing import TypeVar
from flask import request
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class """
