
## 에라토스테네스의 체

def prime_list(min_num, max_num):    ## 0, 1을 확실하게 False로 간주하는 것이 좋다.
    sieve = [False, False] + [True] * (max_num-1)  # 모든 수를 소수로 간주(초기화)

    m = int(max_num ** 0.5)   # n의 최대 약수가 sqrt(n) 이하이므로, i=sqrt(n) 까지 검사
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i*2, max_num+1, i):
                sieve[j] = False

    return [i for i in range(min_num, max_num+1) if sieve[i] == True]

min_num = int(input())
max_num = int(input())

result = prime_list(min_num, max_num)

if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])


