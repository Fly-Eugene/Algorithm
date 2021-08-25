from collections import deque

S = int(input())

time = 0
cnt = 1
clip = 0
dp = [[-1]*(50000) for _ in range(2)]


queue = deque()
queue.append([time, cnt, clip])
res = 0

while queue:
    time, cnt, clip = queue.popleft()
    if cnt == S:
        res = time
        break

    if dp[0][cnt] != -1:
        if dp[1][cnt] == clip:    # 이미 한 번 왔던 갯수 && 클립보드 저장개수까지 똑같다? 더 고려 X
            continue
        else:                   # 이미 한 번 왔는데, 클립보드 갯수가 달라 == 2, 3번 행동 진행
            # 행동 2,3번
            if clip != 0:
                queue.append([time + 1, cnt + clip, clip])
            if cnt > 0:
                queue.append([time + 1, cnt - 1, clip])

    else:
        dp[0][cnt] = time
        dp[1][cnt] = clip

        # 행동1
        queue.append([time+1, cnt, cnt])
        # 행동2
        if clip != 0:
            queue.append([time+1, cnt+clip, clip])
        # 행동3
        if cnt > 0:
            queue.append([time+1, cnt-1, clip])

print(res)
