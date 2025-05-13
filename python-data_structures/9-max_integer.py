def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for num in my_list[1:]:
        if num > max_val:
            max_val = num
    return max_val
print(max_integer([1, 3, 5, 2, 9, 0]))
print(max_integer([]))
print(max_integer([-10, -50, -3]))
