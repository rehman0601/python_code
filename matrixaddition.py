def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

def matrix_print(matrix):
    for row in matrix:
        print(row)
# Input matrices
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
print("Enter elements for Matrix 1:")
matrix1 = matrix_input(rows, cols)
print("Matrix 1:")
matrix_print(matrix1)

matrix2 = []
print("Enter elements for Matrix 2:")
matrix2 = matrix_input(rows, cols)
print("Matrix 2:")
matrix_print(matrix2)

# Perform addition
result_matrix = add_matrices(matrix1, matrix2)
print("Resultant Matrix after addition:")
matrix_print(result_matrix)
