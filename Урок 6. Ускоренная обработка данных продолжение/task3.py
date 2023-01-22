

""" Создайте программу для игры в ""Крестики-нолики"". """
""" Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension """




import random
def print_feeld(play_feeld):
    for row in play_feeld:
        print(" ".join([cell == 1 and "." or cell ==
              2 and "X" or "O" for cell in row]))


def get_coords():
    coords = [0, 0]
    coords = [int(input("Enter 'line' = "))-1,
              int(input("Enter 'collum' = "))-1]
    return coords


def check_free_space(play_feeld):
    return sum([sum([1 for cell in row if cell == 1]) for row in play_feeld])


def get_ai_coords(play_feeld):
    free_space = [(i, j) for i, row in enumerate(play_feeld)
                  for j, cell in enumerate(row) if cell != 2 and cell != 3]
    coords = free_space[random.randint(0, len(free_space)-1)]
    return coords


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
