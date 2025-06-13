def raise_exception():
    raise TypeError("Type exception raised")
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
