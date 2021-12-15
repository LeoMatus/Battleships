import random

grid = []
ship = []
grid_size = 10
rows, cols = (grid_size, grid_size)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
ship_hit = "X"
water_hit = "~"
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

def check_if_input_is_valid(input):
    if len(input) < 2 or len(input) > 2:
        return False
        
    if not input[0].isalpha() or not input[1].isnumeric():
        return False
        


def start_game():
    create_grid()
    print_grid()
    fire_missile()

def fire_missile():
    missile_placement = False

    while missile_placement is False:
        shot_placed = input("Choose a coordinate such as B5 to fire your missile: ")
        shot_placed = shot_placed.upper()
        row = None
        if check_if_input_is_valid(shot_placed) == False:
            print("Your selected coordinates need to concist of one letter and one number!")
            continue

        for i in range(len(alphabet)):
            if shot_placed[0] == alphabet[i]:
                row = i
                break 
        col = int(shot_placed[1])-1
        
        if grid[row][col] == ".":
            grid[row][col] = "X"
            print_grid()
        

start_game()


#gör input till int -1 för att träffa rätt index, ex A1 = [0][0], converta också alphabetiska tecken till index positioner.