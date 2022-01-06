
def factorial(N):
    if fact_list[N-1] != 0:
        fact_list[N] = fact_list[N-1] * N
        return fact_list[N]
    else:
        fact_list[N] = factorial(N-1) * N
        return fact_list[N]


N, K = map(int, input().split())
fact_list = [0] * (N+1)
fact_list[0], fact_list[1] = 1, 1
factorial(N)

res = fact_list[N] // (fact_list[K] * fact_list[N-K])
res %= 10007

print(res)