
s, e = map(int, input().split())

if s < e:
    for i in range(s, e+1):
        for j in range(1, 10):
            if j % 3:
                res = i*j
                if res < 10:
                    print(i, '*', j, '= ', res, end='   ')
                else:
                    print(i, '*', j, '=', res, end='   ')
            else:
                res = i*j
                if res < 10:
                    print(i, '*', j, '= ', res)
                else:
                    print(i, '*', j, '=', res)
        print()
else:
    for i in range(s, e-1, -1):
        for j in range(1, 10):
            if j % 3:
                res = i*j
                if res < 10:
                    print(i, '*', j, '= ', res, end='   ')
                else:
                    print(i, '*', j, '=', res, end='   ')
            else:
                res = i*j
                if res < 10:
                    print(i, '*', j, '= ', res)
                else:
                    print(i, '*', j, '=', res)
        print()