n = int(input())
matrix = []
sum_primary_diagonals = 0
for _ in range(n):
        matrix.append([int(el) for el in input().split()])

for rows in range(n):
    for col in range(n):
        if rows == col:
            sum_primary_diagonals += matrix[rows][col]
print(sum_primary_diagonals)