"""
@Copyrights 2020 Rakesh Kumar T
author: Rakesh Kumar T
github: rakesht2499
"""

import sys
import traceback


class InvalidIpException(Exception):
    __module__ = Exception.__module__
    sys.excepthook = lambda type, value, tb: traceback.print_last(1)

    def __init__(self, *args):
        if args:
            self.msg = args[0]
        else:
            self.msg = None

    def __str__(self):
        if self.msg:
            return "{}".format(self.msg)
        else:
            return "Error has been raised"
