
def pibo(n):
    if n == 0 or n == 1:
        memo[n] = n
        return n
    elif memo[n] != -1:
        return memo[n]
    else:
        memo[n] = pibo(n-1) + pibo(n-2)
        return memo[n]


n = int(input())
memo = [-1] * (n+1)

pibo(n)
print(memo[n])

