
N = int(input())
num_list = list(map(int, input().split()))
dp = list(num_list)    # 기본적으로 num_list 를 복사했음


temp = 0
for i in range(N):
    if dp[i] <= temp + num_list[i]:    # 더해진 값이 dp에 기록된 것보다 크면
        dp[i] = temp + num_list[i]      # 새롭게 dp 에 기록
        temp = dp[i]                   # temp 도 갱신
    else:
        temp = dp[i]      # 더해진 값이 작아? (== dp 기록이 더 커) 그러면 여기서부터 새로 시작

print(max(dp))

