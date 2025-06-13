def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
safe_print_integer(42)
safe_print_integer("hello")  
safe_print_integer(3.14)

