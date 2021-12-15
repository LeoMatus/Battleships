grid = []
grid_size = 10
rows, cols = (grid_size, grid_size)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
ship_hit = "X"
water_hit = "M"
missiles_left = 50



def create_grid():
    for row in range(rows):
        grid.append([])
        for colum in range(cols):
            grid[row].append(".")

def print_grid():
    print("   ", end="")

    for col in range(cols):
        print(col + 1, end=" ")

    print("")

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            print(grid[row][col], end=" ")
        print("")

def start_game():
    create_grid()
    print_grid()
    fire_missile()

def fire_missile():
    missile_placement = False

    while missile_placement is False:
        shot_placed = input("Choose a coordinate such as B5 to fire your missile: ")
        shot_placed = shot_placed.upper()
        row = shot_placed[0]
        col = shot_placed[1]
        print(row)
        print("")
        print(col)
        
    
    

start_game()
grid[0][2] = 0
print_grid()
fire_missile()

#gör input till int -1 för att träffa rätt index, ex A1 = [0][0], converta också alphabetiska tecken till index positioner.