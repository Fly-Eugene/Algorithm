
from itertools import combinations_with_replacement

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]
lion = [0] * 11
score = [i for i in range(11)]
win_list = []
max_diff = 0

res_list = combinations_with_replacement(score, n)
for res in res_list:
    lion = [0] * 11
    for r in res:
        lion[10-r] += 1
        # print(lion)

    a_score, l_score = 0, 0
    for i in range(11):
        if info[i] < lion[i]:
            l_score += 10-i
        else:
            if info[i] != 0:
                a_score += 10-i

    if a_score < l_score:
        print('============================================')
        print('max_score', l_score, a_score)
        print('현재 max_diff', max_diff)

        if max_diff < l_score - a_score:
            max_diff = l_score - a_score
            win_list = lion

        elif max_diff == l_score - a_score:
            if win_list:
                for j in range(10, -1, -1):
                    if win_list[j] < lion[j]:
                        win_list = lion
                        break
                    elif lion[j] < win_list[j]:
                        break
                    else:
                        continue
                # if ''.join(map(str, win_list)) > ''.join(map(str, lion)):
                #     win_list = lion
            else:
                win_list = lion

if win_list:
    answer = win_list
else:
    answer = [-1]

print(answer)





