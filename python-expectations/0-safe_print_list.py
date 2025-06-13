def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
my_list = [1, 2, "f", "d"]
print("Printed:", safe_print_list(my_list, 6))
