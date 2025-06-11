def search_replace(my_list, search, replace):
    return [replace if element == search else element for element in my_list]
my_list = [1, 2, 3, 2, 4]
new_list = search_replace(my_list, 2, 9)

print("Original:", my_list)
print("Modified:", new_list)
