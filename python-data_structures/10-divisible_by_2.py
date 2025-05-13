def divisible_by_2(my_list=[]):
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
print(divisible_by_2([1, 2, 3, 4, 5, 6]))
