#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import signal
import sys


# http://stackoverflow.com/questions/22077881/yes-reporting-error-with-subprocess-communicate
def restore_signals(): # from http://hg.python.org/cpython/rev/768722b2ae0a/
    signals = ('SIGPIPE', 'SIGXFZ', 'SIGXFSZ')
    for sig in signals:
        if hasattr(signal, sig):
            signal.signal(getattr(signal, sig), signal.SIG_DFL)

def check_series():
    if open("series").readline().strip() != "# Kernel patches configuration file":
        print("Error: series file does not look like series.conf",
              file=sys.stderr)
        return False
    else:
        return True
