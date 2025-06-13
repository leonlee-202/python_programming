def raise_exception_msg(message=""):
    raise NameError(message)
try:
    raise_exception_msg("This is a name error!")
except NameError as e:
    print("Caught an exception:", e)
