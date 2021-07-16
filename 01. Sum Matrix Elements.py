rows, columns = [int(el) for el in input().split(", ")]
matrix = []
sum_elements = 0
for row in range(rows):
    matrix.append([int(nums) for nums in input().split(", ")])
    sum_elements += sum(matrix[row])
print(sum_elements)
print(matrix)