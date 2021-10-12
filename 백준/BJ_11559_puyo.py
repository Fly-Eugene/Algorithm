
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bomb_check(col, r, c):
    global visited, bomb_cnt

    queue = [(r, c)]
    candi = []
    visited[r][c] = 1

    while queue:
        r, c = queue.pop(0)
        candi.append((r, c))

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 12 and 0 <= nc < 6:
                if visited[nr][nc] == 0 and arr[nr][nc] == col:  # 아직 방문 안하고, 상하좌우 중 컬러가 동일하다면
                    visited[nr][nc] = 1
                    queue.append((nr, nc))

    if len(candi) >= 4:
        bomb_cnt += 1
        bomb(candi)
        return


def bomb(history):
    global arr
    # print('터트려보자!!!!')

    for item in history:
        r, c = item
        arr[r][c] = '.'


def bomb_down(arr):
    for j in range(6):
        find_color = 11
        for i in range(11, -1, -1):
            if arr[i][j] == '.':
                continue
            else:
                if find_color != i:
                    arr[find_color][j] = arr[i][j]
                    arr[i][j] = '.'
                find_color -= 1


## 입력값 받기
arr = []
for i in range(12):
    arr.append(list(input()))

## 해당 연쇄에서 4개이상 연결된 포지션 터트리기
## bomb를 한 번 돌 때마다 visited 는 new arr로 넣어줘야 한다...!!

cnt = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    bomb_cnt = 0

    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                ## bomb_check(col, r, c, depth, visited)
                bomb_check(arr[i][j], i, j)

    ## 터트린 후, 맨 밑으로 내리기
    bomb_down(arr)

    # for i in range(12):
    #     print(arr[i])

    # print('================================================')

    if bomb_cnt == 0:
        break
    else:
        cnt += 1


print(cnt)
