
N = int(input())
boxes = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    size = boxes[i]
    max_size = 0
    max_cnt = 0
    for j in range(i-1, -1, -1):
        if boxes[j] < size: # 박스의 크기가 작을 때,
            if max_size < boxes[j] and max_cnt < dp[j]: # 앞쪽으로 가면서 현재 최대의 사이즈보다 크면서, 상자 보유 갯수도 큰걸 찾는다.
                max_size, max_cnt = boxes[j], dp[j]
        else:
            continue
    dp[i] = max_cnt + 1

print(max(dp))




