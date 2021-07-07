
def factorial(N):
    global res

    if N == 1:
        print('1! = 1')
        return res

    print(f'{N}! = {N} * {N-1}!')
    res *= N
    factorial(N-1)

N = int(input())
res = 1
factorial(N)
print(res)
