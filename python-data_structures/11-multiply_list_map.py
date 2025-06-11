def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
result = multiply_list_map([1, 2, 3, 4], 3)
print(result)
