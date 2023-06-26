#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = float(a / b)
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
