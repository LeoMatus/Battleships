grid = []
grid_size = 10
rows, cols = (grid_size, grid_size)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    

for row in range(rows):
    grid.append([])
    for colum in range(cols):
        grid[row].append(".")


print("   ", end="")

for col in range(cols):
    print(col + 1, end=" ")

print("")

for row in range(len(grid)):
    print(alphabet[row], end=") ")
    for col in range(len(grid[row])):
        print(grid[row][col], end=" ")
    print("")   
    

