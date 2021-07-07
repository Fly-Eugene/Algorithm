
def tri_1(num):

    for i in range(num):
        if i <= num // 2:
            print('*'*(i+1))
        else:
            print('*'*(num-i))

def tri_2(num):

    for i in range(num):
        if i <= num // 2:
            print(' '*(num//2 - i), end = '')
            print('*'*(i+1))
        else:
            print(' '*(i - num//2), end = '')
            print('*'*(num - i))

def tri_3(num):
    for i in range(num):
        if i <= num // 2:
            print(' '*i, end = '')
            print('*'*(2*(num//2 - i) + 1))
        else:
            print(' '*(num-i-1), end = '')
            print('*'*(2*(i - (num//2)) + 1))

def tri_4(num):
    for i in range(num):
        if i <= num // 2:
            print(' ' * i, end = '')
            print('*' * (num//2 - i + 1))
        else:
            print(' ' * (num // 2), end = '')
            print('*' * (i + 1 - (num // 2)))


n, m = map(int, input().split())

if 0 < n <= 100 and 1 <= m <= 4 and n % 2:

    if m == 1:
        tri_1(n)
    elif m == 2:
        tri_2(n)
    elif m == 3:
        tri_3(n)
    else:
        tri_4(n)
else:
    print("INPUT ERROR!")