
def calc(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return calc(20, 20, 20)

    elif dp[a][b][c] != 0:
        return dp[a][b][c]

    elif a < b and b < c:
        dp[a][b][c] = calc(a, b, c-1) + calc(a, b-1, c-1) - calc(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = calc(a-1, b, c) + calc(a-1, b-1, c) + calc(a-1, b, c-1) - calc(a-1, b-1, c-1)
        return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if (a == -1 and b == -1 and c == -1):
        break

    dp = [[[0] * (21)  for _ in range(21)] for _ in range(21)]
    print(f'w({a}, {b}, {c}) =', calc(a, b, c))
