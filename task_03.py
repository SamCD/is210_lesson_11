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
        except IOError as err:
            self.log('Could not open!')
            raise err

        try:
            for index, entry in enumerate(self.msgs):
                try:
                    fhandler.write(str(entry) + '\n')
                except IOError as err:
                    raise err
                except Exception as err:
                    self.log(err.args[0])
                else:
                    handled.append(index)
        except IOError as err:
            self.log('Had an IOError while processing log files.')
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
