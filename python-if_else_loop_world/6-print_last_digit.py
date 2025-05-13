def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
print_last_digit(7689)
print_last_digit(54)
print_last_digit(2006)
print_last_digit(100)