# import sys
# sys.setrecursionlimit(3500)
#
#
# def perm(idx):
#     if idx == g:
#         print(sel)
#         w_perm_list.append(''.join(sel))
#         return
#     else:
#         for i in range(g):
#             if visited[i] == 0:
#                 if i == 0 or w[i-1] != w[i] or visited[i-1]:
#                     sel[idx] = w[i]
#                     visited[i] = 1
#                     perm(idx + 1)
#
#                     visited[i] = 0
#
#
# g, s = map(int, input().split())
# w = list(input())
# s_word = input()
#
# sel = [0] * g
# visited = [0] * g
# w_perm_list = []
#
# perm(0)
# res = 0
# for i in range(s-g+1):
#     part = s_word[i:i+4]
#     if part in w_perm_list:
#         res += 1
#
# print(res)

## =======================================================================================================================

g, s = map(int, input().split())
w = list(input())
s_word = list(input())
w.sort()

res = 0
for i in range(s-g+1):
    part = s_word[i:i+4]
    part.sort()
    if ''.join(w) == ''.join(part):
        res += 1

print(res)









