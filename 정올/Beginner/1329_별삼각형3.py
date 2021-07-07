
N = int(input())

if 1 <= N <= 100 and N % 2:

    for i in range(N):
        if i <= N // 2:
            print(' ' * i, end = '')
            print('*' * (2*i + 1))
        else:
            print(' ' * (N - i - 1), end = '')
            print('*' * (2 * (N - i-1) + 1))
else:
    print("INPUT ERROR!")
