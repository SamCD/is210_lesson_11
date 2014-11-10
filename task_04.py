#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""

class BaseException(Exception): pass
class StringError(BaseException, TypeError): pass
class NumberError(BaseException, TypeError): pass
class NonZeroError(NumberError): pass
