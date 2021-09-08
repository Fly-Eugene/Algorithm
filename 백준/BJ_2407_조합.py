
def facto(n):
    if n == 0 or n == 1:
        memo[n] = 1
        return 1

    if memo[n] == 0:
        memo[n] = facto(n-1) * n
        return memo[n]


n, m = map(int, input().split())
memo = [0] * (n+1)
facto(n)

res = memo[n] // (memo[m] * memo[n-m])
print(res)





