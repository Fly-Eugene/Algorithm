
from itertools import combinations
import sys
input = sys.stdin.readline

def play_game(round):
    global res

    if round == 15:
        for i in range(6):
            if sum(game_result[i]) != 0:
                return
        res = 1
        return

    n1, n2 = comb_list[round]
    for r1, r2 in [(0, 2), (1, 1), (2, 0)]:
        if game_result[n1][r1] > 0 and game_result[n2][r2] > 0:
            game_result[n1][r1] -= 1
            game_result[n2][r2] -= 1

            play_game(round + 1)
            game_result[n1][r1] += 1
            game_result[n2][r2] += 1


comb_list = list(combinations(range(6), 2))
for i in range(4):
    game_input = list(map(int, input().split()))
    game_result = [[0, 0, 0] for _ in range(6)]
    res = 0

    for j in range(18):
        gi = game_input[j]
        game_result[j//3][j%3] = gi

    play_game(0)
    print(res, end=' ')





