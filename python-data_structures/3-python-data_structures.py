def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
my_numbers = [10, 20, 30, 40]
print_reversed_list_integer(my_numbers)
