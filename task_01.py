#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """Accessing dictionary key"""
    try:
        ret = var1[var2]
    except (LookupError):
        print "Warning: Your key doesn't exist."
        ret = var1
    return ret
