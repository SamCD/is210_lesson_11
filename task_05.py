#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CustomError(Exception):
    def __init__(self, msg, cause):
        Exception.__init__(self, msg)
        self.cause = cause
