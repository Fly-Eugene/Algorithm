def dp(idx):
    global r
    print('현재 idx는', idx)

    if idx == M - N:
        print('지금 idx 1로 반환할거', idx)
        combine_list[idx] = 1
        return 1
    elif combine_list[idx] == 0:
        print('지금 idx 재귀 들어갈거', idx)
        print('곱하는 값은?', idx//(idx-r))
        combine_list[idx] = dp(idx-1) * (idx // (idx-r))
        return combine_list[idx]
    else:
        print('지금 ', idx)
        return combine_list[idx]


N, M = map(int, input().split())

r = N - 1
combine_list = [0] * (M+1)
dp(M)

print(combine_list)
print(sum(combine_list))
