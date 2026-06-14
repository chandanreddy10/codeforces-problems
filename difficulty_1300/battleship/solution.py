import sys

n, k = map(int, sys.stdin.readline().split())

grid = []
for _ in range(n):
    row = sys.stdin.readline().strip()
    grid.append([1 if c == '#' else 0 for c in row])

count_poss = {}
empty_zeros = [0 for _ in range(k)]

for row in range(n):
    for col in range(n):
        count_poss.update({(row, col):0})

for row_index, row in enumerate(grid):
    
    for col_index, col in enumerate(row):
        # print("row",row_index, "column",col_index)
        vertical = grid[row_index:row_index + k]
        # #print(vertical)
        # print("element",grid[row_index][col_index])
        if grid[row_index][col_index] == 1:
            continue
        
        else:
            horizontal = grid[row_index][col_index:col_index + k]
            vertical = [row[col_index] for row_idx, row in enumerate(grid) if row_idx >= row_index][:k]

            # print("Horizontal", horizontal)
            
            # print("vertical",vertical)
            # print("vertical count",vertical_count)
            if horizontal == empty_zeros:
                
                for i in range(k):
                    count_poss[(row_index, col_index + i)] += 1
            
            if vertical == empty_zeros:
                
                for i in range(k):
                    count_poss[(row_index + i, col_index)] += 1
            

        # print("count",count_poss)
        # print("\n")

key = max(count_poss, key=count_poss.get)
print(key[0]+1, key[1]+1)