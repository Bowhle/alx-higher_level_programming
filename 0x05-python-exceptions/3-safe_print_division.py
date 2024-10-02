#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a / b  # Attempt to divide a by b
    except ZeroDivisionError:
        div = None  # If b is zero, set result to None
    finally:
        print("Inside result: {}".format(div))  # Print result inside the finally block
    return div  # Return the result
