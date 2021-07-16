n = int(input())
matrix = []
for row in range(n):
    matrix.append([int(el) for el in input().split()])
bombs = [symb for symb in input().split()]

index = 0
for coords in range(len(bombs)):
    bomb_coord = bombs[index]
    row = int(bomb_coord[0])
    col = int(bomb_coord[2])
    bomb = matrix[row][col]
