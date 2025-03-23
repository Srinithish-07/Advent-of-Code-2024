grid = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]
count = 0




for i in range(len(grid)):
    row = grid[i]
    is_increasing = all(row[j] < row[j+1] for j in range(len(row)-1))
    is_decreasing = all(row[j] > row[j+1] for j in range(len(row)-1))
    is_safe = True

    for j in range(len(row)-1):
        diff = abs(row[j] - row[j+1])
        if diff < 1 or diff > 3:
            is_safe = False
            break

    if (is_increasing or is_decreasing) and is_safe:
        count += 1   
        
    # if(is_increasing or is_decreasing) and is_safe:
    #     print(f"row : {i+1} is safe")
    # else:
    #     print(f"row : {i+1} is unsafe")        

print(count)
