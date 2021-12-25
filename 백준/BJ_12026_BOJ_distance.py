
N = int(input())
blocks = list(input())
dp = [-1] * N
dp[0] = 0

boj = [0, 'B', 'O', 'J']

for i in range(N):

    next = boj[boj.index(blocks[i]) % 3 + 1]

    for j in range(i+1, N):
        if blocks[j] == next and dp[i] != -1:
            energy = (j - i) ** 2
            sum_energy = dp[i] + energy

            if dp[j] == -1:  #새로운 에너지라면
                dp[j] = sum_energy
            else: # 이미 있는 값과 비교해, 최소 에너지 값을 선택
                dp[j] = min(dp[j], sum_energy)

        else: continue

print(dp[N-1])