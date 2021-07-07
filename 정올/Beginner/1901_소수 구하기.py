import math

def isPrime(num):

    for i in range(2, int(math.sqrt(num))+1):
        if is_prime[i] == 0:
            check = i*i
            while check <= num:
                is_prime[check] = 1
                check += i
        else:
            continue


for tc in range(int(input())):
    num = int(input())
    is_prime = [-1, -1] + [0]*(num*2 - 1)

    isPrime(num * 2)

    res = []
    for i in range(num+1):
        if is_prime[num-i] == 0:
            res.append(num-i)
        if is_prime[num+i] == 0:
            if res.count(num+i) == 0:
                res.append(num+i)
        if len(res):
            break

    print(*res)


