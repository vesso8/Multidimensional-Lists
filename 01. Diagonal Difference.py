n = int(input())
matrix = []
sum_primary_diagonals = 0
for row in range(n):
        matrix.append([int(el) for el in input().split()])

secondary_diagonal = 0
counter = n -1
for row in range(n):
    for col in range(n):
        if row == col:
            sum_primary_diagonals += matrix[row][col]
        if col == counter:
            secondary_diagonal += matrix[row][col]
            counter -= 1
result = abs(sum_primary_diagonals-secondary_diagonal)
print(result)