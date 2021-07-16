import sys
rows , columns = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split()])
max_sum = -sys.maxsize
for r in range(0,rows-2):
    for c in range(0,columns-2):
        current_sum = matrix[r][c]+matrix[r][c+1]+matrix[r][c+2]+matrix[r+1][c]+matrix[r+1][c+1]+matrix[r+1][c+2]+matrix[r+2][c]+matrix[r+2][c+1]+matrix[r+2][c+2]
        if current_sum > max_sum:
            max_sum = current_sum
            current_position = (r,c)
r , c = current_position
print(f"Sum = {max_sum}")
print(matrix[r][c] , matrix[r][c+1], matrix[r][c+2])
print(matrix[r+1][c], matrix[r+1][c+1], matrix[r+1][c+2])
print(matrix[r+2][c], matrix[r+2][c+1], matrix[r+2][c+2])