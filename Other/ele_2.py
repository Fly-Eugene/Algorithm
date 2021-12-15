
S = "babaa"
fragment = []
cnt = 1

for i in range(1, len(S)):

    if S[i-1] == S[i]:
        cnt += 1

    else:
        fragment.append(cnt)
        cnt = 1

fragment.append(cnt)
max_cnt = max(fragment)
fragment.sort()

res = 0
for i in range(len(fragment)):

    diff = max_cnt - fragment[i]
    if diff == 0:
        break
    else:
        res += diff


print(fragment)
print(res)