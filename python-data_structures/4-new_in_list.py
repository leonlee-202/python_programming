def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    new_list = my_list[:]  # create a shallow copy
    new_list[idx] = element
    return new_list
original = [1, 2, 3, 4, 5]
new = new_in_list(original, 2, 99)

print("Original:", original)
print("New:", new)
