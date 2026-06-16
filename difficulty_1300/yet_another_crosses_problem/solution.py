from collections import Counter

q = int(input().strip())

for _ in range(q):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    min_cost = []
    count_rows, count_columns = 0, 0
    for row_indx, row_outer in enumerate(grid):
        
        for col_indx, col in enumerate(row_outer):
            column = [row[col_indx] for row in grid]

            rc = row_outer.count(".")
            cc = column.count(".")
        
            total_cost = rc + cc
            if grid[row_indx][col_indx] == ".":
                total_cost -= 1 

            min_cost.append(total_cost)
        
    print(min(min_cost))
