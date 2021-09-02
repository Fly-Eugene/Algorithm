
N = int(input())
goals = []
for _ in range(N):
    goals.append(list(input().split()))


time_diff = 0  # 앞 idx와 시간 차를 저장하는 변수
last_diff = 0  # 48분과 마지막 골의 시간 차를 저장하는 변수
a_cnt, b_cnt = 0, 0  # 각 팀의 골 개수
res_a, res_b = 0, 0  # 각 팀이 이기고 있는 시간 저장 변수

for idx in range(0, N):
    team, time = goals[idx]
    min, sec = time.split(':')
    min = int(min)
    sec = int(sec)

    # 마지막 골이라면 48분과의 차이 시간을 구해준다
    if idx == N-1:
        last_diff = 48 * 60 - (min * 60 + sec)

    # 첫 번째 골이라면 비교할 전 idx가 없으므로 team_cnt만 높여준다.
    if idx == 0:
        if team == '1':
            a_cnt += 1
        else:
            b_cnt += 1

    else:
        pre_time = goals[idx-1][1]
        pre_min, pre_sec = pre_time.split(':')
        pre_min = int(pre_min)
        pre_sec = int(pre_sec)

        # 이전 idx와 시간차이는 ?
        time_diff = (min * 60 + sec) - (pre_min * 60 + pre_sec)

        # 현재 골 상황을 비교하고 res에 더해준다.
        if a_cnt > b_cnt:
            res_a += time_diff
        elif b_cnt > a_cnt:
            res_b += time_diff

        # 이번에 골을 넣은 팀의 개수를 갱신한다.
        if team == '1':
            a_cnt += 1
        else:
            b_cnt += 1

# 48 - 마지막 골 시간을 누구에게 더해줄 것인가.
if a_cnt < b_cnt:
    res_b += last_diff
elif b_cnt < a_cnt:
    res_a += last_diff

# 2자리 수 맞춰주고, str로 변경하는 과정
res = [res_a // 60, res_a % 60, res_b // 60, res_b % 60]
for i in range(4):
    r = res[i]
    if len(str(r)) == 1:
        r = '0' + str(r)
    res[i] = str(r)

print(res[0] + ':' + res[1])
print(res[2] + ':' + res[3])

