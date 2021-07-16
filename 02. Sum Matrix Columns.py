rows, columns = [int(el) for el in input().split(", ")]
matrix = []
for row in range(rows):
    matrix.append([int(nums) for nums in input().split()])
for col in range(columns):
    current_sum = 0
    for r in range(rows):
        current_sum += matrix[r][col]
    print(current_sum)
