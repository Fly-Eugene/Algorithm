
n = int(input())
if n == 0 or n == 1:
    print(n)
else:
    pibo = [0] * (n+1)
    pibo[1] = 1

    for i in range(2, n+1):
        pibo[i] = pibo[i-1] + pibo[i-2]

    print(pibo[n])

