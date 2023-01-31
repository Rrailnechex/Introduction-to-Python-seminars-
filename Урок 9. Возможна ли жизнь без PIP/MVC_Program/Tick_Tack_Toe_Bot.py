import random
import telegram
from tabulate import tabulate

""" 5710530652:AAFyaKIKtJv2BxcJldBzvccxJHRB4rheR_Q """


def main():
    grid = create_grid()
    print("You are playing for X!")

    # turns
    while True:
        print_grid(grid)
        turn_player(grid)
        turn_ai(grid)
        check_win(grid)


def create_grid():
    a = [["", "", ""],
         ["", "", ""],
         ["", "", ""],]
    return a


def print_grid(grid):
    print(tabulate(grid, tablefmt="rounded_grid"))
    """ , tablefmt="orgtbl", missingval="" """


def turn_player(grid):
    print("select cell")
    row = int(input("row = "))
    collum = int(input("collum = "))

    # check if exit outside of range
    while (row > 2 or row < 0) or (collum > 2 or collum < 0):
        print("chosen cell is outside of range! Chose another one!")
        turn_player(grid)

    # checking if input = a busy cell
    while grid[row][collum] != "":
        print("chosen cell is already selected! Chose another one!")
        turn_player(grid)

    grid[row][collum] = "X"
    return grid


""" def get_ai_coords(play_feeld):
    free_space = []

    for i in range(len(play_feeld[0])):
        for j in range(len(play_feeld[1])):
            if play_feeld[i][j] != 2 and play_feeld[i][j] != 3:
                free_space.append([i, j])

    coords = [free_space[random.randint(0, len(free_space)-1)]]
    coords2 = [coords[0][0], coords[0][1]]
    return coords2 """


def turn_ai(grid):
    # check end
    if check_for_free_spase(grid) != 0:
        # get free cells
        free_space = []
        for i in range(len(grid[0])):
            for j in range(len(grid[1])):
                if grid[i][j] == "":
                    free_space.append([i, j])

        # chose on of free cells
        coords = [free_space[random.randint(0, len(free_space)-1)]]

        # set O
        #grid[coords[0][0]][coords[0][1]] = "O"
        grid[coords[0][0]][coords[0][1]] = "O"
        return grid
    else:
        pass


def check_for_free_spase(grid):
    free_space = 0
    for i in range(len(grid[0])):
        for j in range(len(grid[1])):
            if grid[i][j] == "":
                free_space += 1
    return free_space


def check_win(grid):
    t = True
    f = False

    # vertical
    v1 = [[t, f, f],
          [t, f, f],
          [t, f, f],]
    v2 = [[f, t, f],
          [f, t, f],
          [f, t, f],]
    v3 = [[f, f, t],
          [f, f, t],
          [f, f, t],]

    # horizontal
    h1 = [[t, t, t],
          [f, f, f],
          [f, f, f],]
    h2 = [[f, f, f],
          [t, t, t],
          [f, f, f],]
    h3 = [[f, f, f],
          [f, f, f],
          [t, t, t],]

    # diagonal
    d1 = [[t, f, f],
          [f, t, f],
          [f, f, t],]
    d2 = [[f, f, t],
          [f, t, f],
          [t, f, f],]

    win_ways = [v1, v2, v3, h1, h2, h3, d1, d2]

    won = "No one"

    # winnings check For X
    gridx = grid
    for i in range(len(gridx)):
        # написать условия победы как-то
        pass

    for i in range(len(win_ways)):
        if gridx == win_ways[i]:
            won = "X is won!!"

    if check_for_free_spase(grid) == 0:
        print("draw!!! No one is won!!!")
        exit()

    if won == "X is won!!":
        print(won)
        exit()
    elif won == "O is won!!":
        print(won)
        exit()


# start program
main()
