
def zero_lf(mid, res):
    while res[mid] == '0':
        mid += 1
    return mid

def zero_rg(mid, res):
    while res[mid] == '0':
        mid -= 1
    return mid


n = '929800275'
res = n
cnt = 0

while len(res) != 1:
    print('===============================')
    print(res)
    mid = len(res) // 2
    cnt += 1

    if res[mid] == '0':
        lf_mid = zero_lf(mid, res)
        rg_mid = zero_rg(mid, res)
        print(lf_mid, rg_mid)
        if lf_mid == 0:
            res1 = 1000000001
        else:
            res1 = int(res[:lf_mid]) + int(res[lf_mid:])
        if rg_mid == 0:
            res2 = 1000000001
        else:
            res2 = int(res[:rg_mid]) + int(res[rg_mid:])

        if res1 < res2:
            res = str(res1)
        else:
            res = str(res2)

    else:
        if len(res) % 2 == 0:
            print('짝수에요', res)
            res = str(int(res[:mid]) + int(res[mid:]))
            print(res)

        else:
            print('홀수에요', res)
            res1 = int(res[:mid+1]) + int(res[mid+1:])
            if res[mid-1] == '0':
                res2 = 1000000001
            else:
                res2 = int(res[:mid]) + int(res[mid:])
            if res1 < res2:
                res = str(res1)
            else:
                res = str(res2)
            print(res)

print([cnt, int(res)])

