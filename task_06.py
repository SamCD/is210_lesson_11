#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 06 module"""

def exception_test(arg1, arg2, arg3):
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, KeyError, IndexError):
        caught = True

    return caught
    
