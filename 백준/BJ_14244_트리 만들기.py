
n, m = map(int, input().split())

for i in range(1, n):
    if i < n-(m-1):
        print(i-1, i)
    else:
        print(n-m, i)

