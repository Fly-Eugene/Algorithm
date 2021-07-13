
def count_hb(idx, time):
    global max_cnt


    l_idx, r_idx = idx, idx
    r_time, l_time = time, time
    cnt = 1

    # idx 왼쪽 부분 탐색
    while l_idx > 0:
        # print('왼쪽 도는 중')
        l_find = False
        i = 1
        while hay_bales[l_idx - i] >= hay_bales[l_idx] - l_time:
            cnt += 1
            i += 1
            l_find = True
            if l_idx - i < 0:
                break
        if l_find:
            # print('왼쪽 한 번에 여기까지', l_idx, l_idx - (i-1))
            l_idx = l_idx - (i-1)
            l_time += 1
        else:
            break


    # idx 오른쪽 부분 탐색
    while r_idx < N-1:
        # print('오른쪽 도는 중')
        r_find = False
        i = 1
        while hay_bales[r_idx + i] <= hay_bales[r_idx] + r_time:
            cnt += 1
            i += 1
            r_find = True
            if r_idx + i > N-1:
                break
        if r_find:
            # print('오른쪽 한 번에 여기까지', r_idx, r_idx + (i - 1))
            r_idx = r_idx + (i-1)
            r_time += 1
        else:
            break

    if max_cnt < cnt:
        max_cnt = cnt




N = int(input())
hay_bales = [int(input()) for _ in range(N)]
hay_bales.sort()
max_cnt = 0

for idx in range(N):
    count_hb(idx, 1)

print(max_cnt)

