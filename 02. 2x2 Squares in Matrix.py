row , column = [int(el) for el in input().split()]
matrix = []

for r in range(row):
    matrix.append([el for el in input().split()])
square_matrix_found = 0
for rows in range(row-1,0,-1):
    for cols in range(column-1,0,-1):
        current_position = matrix[rows][cols]
        next_position = matrix[rows][cols-1]
        under_position = matrix[rows-1][cols]
        under_right_position = matrix[rows-1][cols-1]
        if current_position == next_position and current_position == under_position and current_position == under_right_position:
            square_matrix_found += 1
print(square_matrix_found)
