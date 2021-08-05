
def check(time, money, idx):
    if idx + time > N:
        return
    else:
        if dp[idx] < money + arr[idx][1]:
            dp[idx] = money + arr[idx][1]       # 지금까지 더한 돈 + 현재 상담돈
            n_money = dp[idx]

        else:        # 현재 가는 루트보다 다른 루트로 돈을 더 많이 벌 수 있으므로 return...퇴장
            return

        for n_idx in range(time + idx, N):
            check(arr[n_idx][0], n_money, n_idx)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)    # 받을 수 있는 최대 금액을 기록할 list

for st in range(N):
    check(arr[st][0], 0, st)

res = max(dp)
print(res)