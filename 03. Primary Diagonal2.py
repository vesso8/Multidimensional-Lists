n = int(input())
matrix = []
sum_primary_diagonals = 0
for row in range(n):
        matrix.append([int(el) for el in input().split()])
        sum_primary_diagonals += matrix[row][row]
print(sum_primary_diagonals)