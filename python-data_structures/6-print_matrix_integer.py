def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end="")
        print()
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print_matrix_integer(matrix)
