#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    ex = 0
    try:
        c = (a / b)
    except Exception:
        ex = 1
    finally:
        if ex == 1:
            print("Inside result: {:s}".format('None'))
            return None
        else:
            print("Inside result: {0:.1f}".format(c))
            return c
