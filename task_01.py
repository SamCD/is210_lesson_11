#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    try:
        ret = var1[var2]
    except IndexError:
        print "Warning: Your index/key doesn't exist."
        ret = var1
    return ret
