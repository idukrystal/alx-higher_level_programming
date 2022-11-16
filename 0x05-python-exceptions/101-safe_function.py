#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        f = fct(*args)
        return f
    except Exception as mess:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
