
N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    prices[i][0] = min(prices[i-1][1], prices[i-1][2]) + prices[i][0]
    prices[i][1] = min(prices[i-1][0], prices[i-1][2]) + prices[i][1]
    prices[i][2] = min(prices[i-1][0], prices[i-1][1]) + prices[i][2]

print(min(prices[N-1]))

