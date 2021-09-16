from collections import deque

def chk_prime(prime, max_n):
    for idx in range(max_n):
        x = 2
        if prime[idx] == 0:
            while idx * x < max_n:
                prime[idx * x] = 1
                x += 1
        else:
            continue

def change_k(num, k):
    res = deque()
    while num >= k:
        share = num // k
        rest = num % k
        res.append(str(rest))
        num = share

    res.append(str(num))
    res.reverse()
    res = ''.join(res)

    return res


max_n = 1000001
# max_n = 20
# prime = deque()
# prime.extend([0] * max_n)
prime = [0] * max_n
prime[0], prime[1] = 1, 1

chk_prime(prime, max_n)

n = 1000000
k = 3
answer = 0

res = change_k(n, k)
res_list = res.split('0')
print(res_list)

for i in range(len(res_list)):
    if res_list[i] == '':
        continue
    else:
        chk_num = int(res_list[i])
        if prime[chk_num] == 0:
            answer += 1

print(answer)