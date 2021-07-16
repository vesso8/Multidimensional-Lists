rows, column = [int(el) for el in input().split()]
matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

if column > row:
    biggest_index = column
else:
    biggest_index = row
command = input()
while not command == "END":
    check_command = command.split()
    valid_coords = True
    if check_command[0] == "swap" and len(check_command) == 5:
        all_nums = check_command[1:]
        for nums in all_nums:
            if int(nums) > biggest_index - 1:
                print("Invalid input!")
                valid_coords = False
                break
    else:
        print("Invalid input!")
        valid_coords = False
    if valid_coords:
        first_row = int(all_nums[0])
        first_col = int(all_nums[1])
        changing_row = int(all_nums[2])
        changing_col = int(all_nums[3])
        new_matrix = matrix[first_row][first_col]
        matrix[first_row][first_col] = matrix[changing_row][changing_col]
        matrix[changing_row][changing_col] = new_matrix
        for symb in matrix:
            print(*symb)
    command = input()