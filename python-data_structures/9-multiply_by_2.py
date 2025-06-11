def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
original_dict = {'a': 1, 'b': 2, 'c': 3}
result = multiply_by_2(original_dict)
print(result)
