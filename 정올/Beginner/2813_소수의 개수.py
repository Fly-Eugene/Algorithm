import math

m, n = map(int, input().split())

cnt = 0
is_prime = [-1, -1] + [0]*(n-1)

for i in range(2, int(math.sqrt(n))+1):
    if is_prime[i] == 0:
        for idx in range(i*i, n+1, i):
            is_prime[idx] = 1

    else: continue

for i in range(m, n+1):
    if is_prime[i] == 0:
        cnt += 1

print(cnt)
