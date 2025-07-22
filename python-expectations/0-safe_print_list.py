def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        return count
    except IndexError:
        return "An error occured"

my_list = [1, 2, "f", "d"]
print("Printed:", safe_print_list(my_list, 6))
