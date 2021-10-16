

S = 'ACBDACBD'

S_list = list(S)
trans_cnt = -1
while True:
    if trans_cnt == 0:
        break

    else:
        trans_cnt = 0
        for i in range(len(S_list)-1):
            if S[i] + S[i+1] in ('AB', 'BA', 'CD', 'DC'):
                S_list[i] = ''
                S_list[i+1] = ''
                trans_cnt += 1

        S = ''.join(S_list)
        S_list = list(S)

print(S)