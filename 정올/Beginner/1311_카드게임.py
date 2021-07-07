
card_list = [[0]*10 for _ in range(4)]

num_cnt = [0]*10

for i in range(5):
    color, num = input().split()
    if color == "R":
        card_list[0][int(num)] = 1
    elif color == "G":
        card_list[1][int(num)] = 1
    elif color == "B":
        card_list[2][int(num)] = 1
    elif color == "Y":
        card_list[3][int(num)] = 1

    num_cnt[int(num)] += 1

score = 0
for clr in range(4):
    if score != 0:
        break
    for i in range(1, 6):
        if card_list[clr][i] == card_list[clr][i+1] == card_list[clr][i+2] == card_list[clr][i+3] == card_list[clr][i+4] == 1:
            score = i + 4 + 900

if score == 0:
    for i in range(1, 10):
        if num_cnt[i] == 4:
            score = i + 800

if score == 0:
    if 3 in num_cnt and 2 in num_cnt:
        score = num_cnt.index(3) * 10 + num_cnt.index(2) + 700

if score == 0:
    for clr in range(4):
        if score != 0:
            break
        if card_list[clr].count(1) == 5:
            for i in range(9, 0, -1):
                if card_list[clr][i] == 1:
                    score = i + 600
                    break

if score == 0:
    for i in range(1, 6):
        if num_cnt[i] == num_cnt[i+1] == num_cnt[i+2] == num_cnt[i+3] == num_cnt[i+4] == 1:
            score = i + 4 + 500

if score == 0:
    if 3 in num_cnt:
        score = num_cnt.index(3) + 400

if score == 0:
    two_cnt = 0
    sm_idx = 0
    for i in range(1, 10):
        if num_cnt[i] == 2:
            two_cnt += 1
            if two_cnt == 1:
                sm_idx = i

            if two_cnt == 2:
                score = i * 10 + sm_idx + 300
                break

if score == 0:
    if 2 in num_cnt:
        score = num_cnt.index(2) + 200

if score == 0:
    for i in range(9, 0, -1):
        if num_cnt[i] == 1:
            score = i + 100
            break

print(score)





