n = int(input())
position = None
matrix = []
for rows in range(n):
    matrix.append(list(input()))
symbol = input()

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == symbol:
            position = (r, c)
            break
    if position:
        break
if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")