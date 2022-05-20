from random import randint

grid = []
ship = []
grid_size = 10
rows, cols = (grid_size, grid_size)
alphabet = "ABCDEFGHIJ"
ship_hit = "X"
water_hit = "~"
missiles_left = 50



def create_grid():
    """
    Creates a 10x10 grid
    """
    for row in range(rows):
        grid.append([])
        for colum in range(cols):
            grid[row].append(".")

def print_grid():
    """
    Prints the grid to the terminal with alphabetical end numerical positions for each coordinate
    """
    print("   ", end="")

    for col in range(cols):
        print(col + 1, end=" ")

    print("")

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "0":
                print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")


def check_if_input_is_valid(input):
    """
    Checks if the user input is valid. it must contain a letter from A-J followed by a number from 1-10
    """
    if len(input) == 3:
        is_ten = int(input[1] + input[2])
        if is_ten != 10:
            return False

    if len(input) < 2 or len(input) > 3:
        return False
   
    if not input[0].isalpha() or input[0] not in alphabet or not input[1].isnumeric():
        return False
        

def start_game():
    """
    This is the main function, it calls upon the other functions for the game to start
    """
    create_grid()
    place_ship(grid)
    print_grid()
    fire_missile()


def fire_missile():
    """
    Fires a missile by taking an input value from the user. If the value is written in the wrong format it gives an error message and asks the user to try again.
    """
    missile_placement = False

    while missile_placement is False:
        shot_placed = input("Choose a coordinate such as B5 to fire your missile: ")
        shot_placed = shot_placed.upper()
        row = None
        if check_if_input_is_valid(shot_placed) is False:
            print("Your selected coordinates need to concist of one letter (A-J) and one number (1-10)!")
            continue

        for i in range(len(alphabet)):
            if shot_placed[0] == alphabet[i]:
                row = i
                break
        
        if len(shot_placed) == 3:
            col = int(shot_placed[1] + shot_placed[2])-1
        else:
            col = int(shot_placed[1])-1

        if grid[row][col] == ".":
            grid[row][col] = "X"
            print_grid()
        if grid[row][col] == "0":
            grid[row][col] = "H"
            print_grid()

def place_ship(grid):
    """
    Places a 3 position long ship randomly on the grid
    """
    orientation = ["h", "v"][randint(0, 1)]

    if orientation == "h":
        x = randint(0, 6)
        y = randint(0, 9)
        grid[y][x] = grid[y][x+1] = grid[y][x+2] = '0'
    if orientation == "v":
        x = randint(0, 9)
        y = randint(0, 6)
        grid[y][x] = grid[y+1][x] = grid[y+2][x] = '0'


start_game()

