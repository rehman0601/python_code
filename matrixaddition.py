def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Input matrices
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = []
print("Enter elements for Matrix 1:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

matrix2 = []
print("Enter elements for Matrix 2:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Perform addition
result_matrix = add_matrices(matrix1, matrix2)
print("Resultant Matrix after addition:")
for row in result_matrix:
    print(row)
