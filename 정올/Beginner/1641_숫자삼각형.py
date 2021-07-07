
def tri_1(n):

    num = 0
    for i in range(n):
        if i % 2 == 0:
            num += i + 1
            for j in range(i+1):
                print(num, end = ' ')
                num += 1
            print()
        else:
            num += i
            for j in range(i+1):
                print(num, end = ' ')
                num -= 1
            print()

def tri_2(n):

    num = 0
    for i in range(n):
        print(' ' * (i*2), end = '')
        arr = [num] * (2 * (n - (i + 1)) + 1)
        print(*arr, sep = ' ')
        num += 1

def tri_3(n):
    for i in range(n):
        num = 1
        if i <= n // 2:
            for j in range(i+1):
                print(num, end = ' ')
                num += 1
        else:
            for j in range(n - i):
                print(num, end = ' ')
                num += 1
        print()



n, m = map(int, input().split())

if 1 <= n <= 100 and 1 <= m <= 3 and n % 2:
    if m == 1:
        tri_1(n)
    elif m == 2:
        tri_2(n)
    else:
        tri_3(n)
else:
    print('INPUT ERROR!')