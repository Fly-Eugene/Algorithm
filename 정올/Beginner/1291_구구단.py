
# 한줄에 s -> e 를 쭉 나타낼 것임
# 1. s -> e 가 양수 증가인지 음수 증가인지 파악
# 2. 2~9 사이의 s,e인지 체크 ==> 아니면 INPUT ERROR 를 출력함

# s * i(1~9) = result (3칸) s+1 * i(1~9) = result (3칸) 을 출력
# 만약 s + 1 이 == e가 되면,

def gugudan():
    s, e = map(int, input().split())
    if 1 < s <= 9 and 1 < e <= 9:

        if s < e:       # s가 e보다 작은경우
            for i in range(1, 10):
                for j in range(s, e+1):
                    res = i*j
                    if res < 10:
                        if j == e:
                            print(j, '*', i, '= ', res, end='')     # print 문에 기본적으로 한칸 띄어쓰기가 있음
                        else:
                            print(j, '*', i, '= ', res, end= '   ')
                    else:
                        if j == e:
                            print(j, '*', i, '=', res, end= '')
                        else:
                            print(j, '*', i, '=', res, end= '   ')
                print()
        else:
            for i in range(1, 10):
                for j in range(s, e-1, -1):
                    res = i * j
                    if res < 10:
                        if j == e:
                            print(j, '*', i, '= ', res, end='')
                        else:
                            print(j, '*', i, '= ', res, end='   ')
                    else:
                        if j == e:
                            print(j, '*', i, '=', res, end= '')
                        else:
                            print(j, '*', i, '=', res, end='   ')
                print()
    else:
        print("INPUT ERROR!")
        gugudan()


gugudan()





