#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CustomError(Exception):
    """Custom error"""

    
    def __init__(self, msg, cause):
        """Error defined"""
        Exception.__init__(self, msg)
        self.cause = cause
