def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
my_list = [5, 10, 15, 20]
print(replace_in_list(my_list, 2, 99))  
print(replace_in_list(my_list, 0, 7))
print(replace_in_list(my_list, -1, 5))
