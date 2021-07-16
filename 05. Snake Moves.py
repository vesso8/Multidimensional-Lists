rows , columns = [int(el) for el in input().split()]
snake = input()
matrix = []
for r in range(rows):
    matrix.append([0 for el in range(columns)])
current_index = 0
for row in range(rows):
    for col in range(columns):
        matrix[row][col] = snake[current_index]
        current_index += 1
        if current_index == len(snake):
            current_index = 0
for row_index in range(rows):
    if row_index % 2 == 1:
        matrix[row_index].reverse()
    print(''.join(matrix[row_index]))
