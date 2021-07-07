import math

def isPrime(num):
    if num == 1:
        return -1

    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return 1
            else: continue

        return 0

num_list = list(map(int, input().split()))

for num in num_list:

    res = isPrime(num)
    if res == -1:
        print('number one')
    elif res == 0:
        print('prime number')
    else:
        print('composite number')

