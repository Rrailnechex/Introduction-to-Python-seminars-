

""" Создайте программу для игры в ""Крестики-нолики"". """


import random


def print_feeld(play_feeld):
    for i in range(len(play_feeld)):
        for j in range(len(play_feeld[i])):
            if play_feeld[i][j] == 1:
                print(".", end=" ")
            elif play_feeld[i][j] == 2:
                print("X", end=" ")
            elif play_feeld[i][j] == 3:
                print("O", end=" ")
        print()


def get_coords():
    coords = [0, 0]
    coords = [int(input("Enter 'line' = "))-1,
              int(input("Enter 'collum' = "))-1]
    return coords


def check_free_space(play_feeld):
    free_space = 0

    for i in range(len(play_feeld[0])):
        for j in range(len(play_feeld[1])):
            if play_feeld[i][j] == 1:
                free_space += 1

    return free_space


def get_ai_coords(play_feeld):
    free_space = []

    for i in range(len(play_feeld[0])):
        for j in range(len(play_feeld[1])):
            if play_feeld[i][j] != 2 and play_feeld[i][j] != 3:
                free_space.append([i, j])

    coords = [free_space[random.randint(0, len(free_space)-1)]]
    coords2 = [coords[0][0], coords[0][1]]
    return coords2


def insert_turn(play_feeld, coords, value):
    play_feeld[coords[0]][coords[1]] = value
    return play_feeld


def game_cycle(play_feeld):
    loop = True
    coords = [0, 0]

    print_feeld(play_feeld)
    while loop == True:

        # players turn
        print(">>> Players turn <<<")
        coords = get_coords()
        insert_turn(play_feeld, coords, 2)
        print_feeld(play_feeld)

        # super AI turn
        print(">>> AIs turn <<<")
        coords = get_ai_coords(play_feeld)
        insert_turn(play_feeld, coords, 3)
        print_feeld(play_feeld)

        # end geme
        loop = False if check_free_space(play_feeld) == 0 else loop


play_feeld = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

print("!!!game started!!!")
game_cycle(play_feeld)
print("!!!game ended!!!")
