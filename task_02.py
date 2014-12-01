#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Invalid Age exception"""
    pass


def get_age(birthyear):
    """Retrieves age or raises InvalidAgeError"""
    age = datetime.datetime.now().year - birthyear
    if age < 0:
        raise InvalidAgeError('You\'re from the future!')
    return age
