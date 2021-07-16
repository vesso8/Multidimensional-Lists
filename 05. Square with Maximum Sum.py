import sys


rows, columns = [int(el) for el in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = -sys.maxsize
for r in range(rows-1, 0 , -1):
    for c in range(columns-1, 0 , -1):
        current_sum = matrix[r][c] + matrix[r][c-1] + matrix[r-1][c-1] + matrix[r-1][c]
        if current_sum >= max_sum:
            max_sum = current_sum
            current_position = (r, c)
r , c = current_position
print(matrix[r-1][c-1], matrix[r-1][c])
print(matrix[r][c-1], matrix[r][c])
print(max_sum)
