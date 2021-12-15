
A = [1, 2, 2, 2, 2, 2, 3, 3, 4]
N = len(A)
cnt = 1
now_num = A[0]
res = 0

def calc(cnt, now_num):
    global res

    ## 가장 적게 +- 하기 위한 연산
    if cnt < now_num:
        half = now_num // 2
        if cnt <= half:
            res += cnt

        else:
            res += now_num - cnt

    elif cnt > now_num:
        res += cnt - now_num



for i in range(1, N):

    ## 같은 숫자들의 반복이 끝났다. X times 맞처주기
    if A[i-1] != A[i] or i == N-1:
        ## 마지막 숫자 반복을 고려하기 위한 ifelse
        if i == N-1 and A[i-1] == A[i]:
            cnt += 1

        elif i == N-1 and A[i-1] != A[i]:
            calc(cnt, now_num)

            now_num = A[i]
            cnt = 1

        calc(cnt, now_num)


        ## reset
        now_num = A[i]
        cnt = 1

    else:
        cnt += 1


print(res)




