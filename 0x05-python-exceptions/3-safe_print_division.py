#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two ints and prints the result.
    You have to use try: / except:
    You have to use "{:d}".format() to print the result.
    The result of the division should print on the finally: section,
    preceded by Inside result:
    Not allowed to import any module

        Args:
            a: Integer
            b: Integer

        Returns: The value of the division, otherwise: None
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
