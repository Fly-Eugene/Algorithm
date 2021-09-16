
board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
N = len(board)
M = len(board[0])

for sk in skill:
    type, r1, c1, r2, c2, dg = sk
    if type == 1:
        dg = -dg

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            board[i][j] += dg

answer = 0
for i in range(N):
    board[i].sort(reverse=True)
    not_destroy = 0
    for j in range(M):
        if board[i][j] > 0:
            not_destroy += 1
        else:
            break

    answer += not_destroy

print(answer)


