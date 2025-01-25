def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix

# Input matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter elements for the matrix:")
matrix = matrix_input(rows, cols)

# Transpose matrix
transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)
