
# N 을 입력받고, 4, 3, 2, 1 개의 공백
#

def chr_num(num):
    num += 64
    while num < 65 or num > 90:
        if num < 65:
            num += 26
        elif num > 90:
            num -= 26

    return chr(num)


N = int(input())

for i in range(1, N+1):
    print(' '*(N-i)*2, end='')
    print(chr_num(i), end=' ')

    res = i + N - 1
    for j in range(N-1, N-i, -1):

        if j == N-1:
            print(chr_num(res), end = ' ')
        else:
            res += j
            print(chr_num(res), end = ' ')

    print()