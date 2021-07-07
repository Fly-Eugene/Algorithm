
N, K = map(int, input().split())

num_list = [i for i in range(1, N+1)]
res = []

p_idx = 0
while len(res) < N:

    p_idx = (p_idx + (K-1)) % len(num_list)
    res.append(num_list.pop(p_idx))

print('<', end = '')
print(*res, sep= ', ', end = '')
print('>')

