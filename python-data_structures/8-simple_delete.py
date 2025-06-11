def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
my_dict = {'name': 'Leon', 'age': 19, 'city': 'Kisumu', 'occupation': 'Student'}

simple_delete(my_dict, 'age')

simple_delete(my_dict, 'country')

print(my_dict)
