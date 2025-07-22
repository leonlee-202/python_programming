def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
my_dict = {'name':'Leon', 'age': 19, }
update_dictionary(my_dict, 'age', 30)
# update_dictionary(my_dict, 'city', 'Rome')
# update_dictionary(my_dict, 'occupation', 'Software Developer')

print(my_dict)
