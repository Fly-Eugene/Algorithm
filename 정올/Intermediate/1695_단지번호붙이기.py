dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    global cnt
    arr[r][c] = -1
    cnt += 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 1:
                dfs(nr, nc)

    return


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


res_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res_list.append(cnt)

print(len(res_list))
for num in sorted(res_list):
    print(num)
