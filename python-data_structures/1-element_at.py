def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
print(element_at([5, 10, 15, 20], 6))
print(element_at([5, 10, 15, 20], 1))
print(element_at([5, 10, 15, 20], -3))
