import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
def divide(a, b):
    return a / b

print(safe_function(divide, 10, 2))
print(safe_function(divide, 10, 0))
