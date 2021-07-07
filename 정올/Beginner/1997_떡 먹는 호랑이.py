def pibo(n):
    global pibo_list

    if pibo_list[n]:
        return pibo_list[n]
    else:
        pibo_list[n] = pibo(n-1) + pibo(n-2)
        return pibo_list[n]



D, K = map(int, input().split())
pibo_list = [1, 1] + [0] * D
pibo(D)

A, B = 0, 0
if D == 3:
    A = 1
    B = K-1
else:
    coff_a = pibo_list[D-3]
    coff_b = pibo_list[D-2]

    for a in range(1, K+1):
        if (K - (a*coff_a)) % coff_b == 0:
            A = a
            B = (K - (a*coff_a)) // coff_b
            break

print(A)
print(B)