def safe_print_list_integers(my_list=[], x=0):
    count = 0
    printed = 0
    try:
        while count < x:
            try:
                print("{:d}".format(my_list[count]), end="")
                printed += 1
            except (ValueError, TypeError):
                pass
            count += 1
    except IndexError:
        pass
    print()
    return printed
my_list = [1, "hello", 2, 3.5, 4]
print(safe_print_list_integers(my_list, 5))
