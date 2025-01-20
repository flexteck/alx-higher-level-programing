#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        result = fct(args[0], args[1])

        return result
    except (ValueError, IndexError, ZeroDivisionError,\
            RuntimeError) as e:
        print("Exception:", e, file=sys.stderr)
        return None
