
N = 6
A = [1, 1, 2, 5]
B = [2, 3, 4, 6]

res = 0
p = [i for i in range(N+1)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    a, b = find_set(x), find_set(y)

    if a < b:
        p[b] = a
    else:
        p[a] = b

## 조합 계산하는 거 만들기
def comb(n, r):

    perm = [0] * (N+1)
    perm[0], perm[1] = 1, 1

    for i in range(2, N+1):
        perm[i] = perm[i-1] * i

    print(perm)
    res = int(perm[n] / (perm[r] * perm[n-r]))
    return res


for i in range(len(A)):
    a, b = A[i], B[i]
    print(a, b)
    union(a, b)

print(p)
res = 0
for parent in range(1, N+1):
    cnt = p.count(parent)
    if cnt == 0: continue
    res += comb(cnt, 2)


temp = comb(5, 2)
print(temp)
print('이게 정답이다!!', res - len(A))



