
S = '?a?'
S_list = list(S)

N = len(S)
left, right = 0, 0

if N // 2 == 1: # N이 홀수일때
    left = N//2 - 1
    right = N//2 + 1

    if S_list[N//2] == '?':
        S_list[N//2] = 'a'

else:
    left = N//2 - 1
    right = N//2

res = ''
while left >= 0:
    if S_list[left] == '?' and S_list[right] == '?':
        S_list[left] = 'a'
        S_list[right] = 'a'

    elif S_list[left] == '?':
        S_list[left] = S_list[right]

    elif S_list[right] == '?':
        S_list[right] = S_list[left]

    else:
        if S_list[left] != S_list[right]:
            res = "NO"
            break

    left -= 1
    right += 1

if res == "NO":
    # return
    print(res)
else:
    res = ''.join(S_list)
    print(res)
