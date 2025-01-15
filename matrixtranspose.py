def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

# Input matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter elements for the matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Transpose matrix
transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)
