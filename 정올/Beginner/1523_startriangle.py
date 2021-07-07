
def tri_1(num):
    for i in range(num):
        print('*'*(i+1))

def tri_2(num):
    for i in range(num):
        print('*'*(num-i))

def tri_3(num):
    for i in range(num):
        print(' '*(num-i-1), end='')
        print('*'*(i*2 + 1))

n, m = map(int, input().split())

if 1<= n <= 100 and 1 <= m <= 3:
    if m == 1:
        tri_1(n)
    elif m == 2:
        tri_2(n)
    else:
        tri_3(n)

else:
    print("INPUT ERROR!")

