#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Logging class"""

    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Creates log"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Flush method"""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except NameError as nerr:
            self.log("{} is invalid".format(self.logfilename))
            raise nerr
        except IOError:
            self.log("error")
        else:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                except NameError("Can/'nt be written") as nerr:
                    raise nerr
                else:
                    handled.append(index)
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
