def square_matrix_simple(matrix=[]):
    return [[element ** 2 for element in row] for row in matrix]
matrix = [[1, 2], [3, 4]]
new_matrix = square_matrix_simple(matrix)

print("Original:", matrix)
print("Squared:", new_matrix)
