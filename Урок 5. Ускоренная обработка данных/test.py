

import random


def get_ai_coords(play_feeld):
    free_space = []

    for i in range(len(play_feeld[0])):
        for j in range(len(play_feeld[1])):
            if play_feeld[i][j] != 2 and play_feeld[i][j] != 3:
                free_space.append([i, j])

    coords = [free_space[random.randint(0, len(free_space)-1)]]
    return coords


play_feeld = [[1, 1, 1], [2, 3, 3], [2, 3, 1]]
print("final", get_ai_coords(play_feeld))
