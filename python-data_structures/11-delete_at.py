def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
my_numbers = [10, 20, 30, 40, 50]

# print(delete_at(my_numbers, 2))
# print(delete_at(my_numbers, 10))
print(delete_at(my_numbers, -1))
