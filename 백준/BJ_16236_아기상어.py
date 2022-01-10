
## 자신보다 큰 물고기가 있는 칸은 지나가지 못한다.
## 같은 크기는 지나갈 수 있고, 작은 크기는 먹을 수 있다.
## 본인의 몸집의 개수만큼 물고기를 먹으면 크기가 커진다.

## (먹을 수 있는) 거리가 가장 가까운 물고기를 먹으러 간다 => bfs
## 거리가 같다면, 상 우선, 좌 우선으로 구분한다.

## 결과 : 몇 초동안 물고기를 다 먹을 수 있는가

##
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move_shark(i, j, visited):
    global sh_size

    queue = deque()
    queue.append((i, j, 0))
    visited[i][j] = 0

    fish_r, fish_c, fish_dis = N, N, N*N

    while queue:
        r, c, dis = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if arr[nr][nc] == sh_size or arr[nr][nc] == 0:  ## 상어의 크기와 물고기의 크기가 같을 때 / 그냥 바다일 때
                    queue.append((nr, nc, dis +  1))
                    visited[nr][nc] = 1

                elif arr[nr][nc] != 0 and arr[nr][nc] < sh_size:  ## 상어의 크기보다 물고기가 작을 때
                    if dis + 1 < fish_dis:  ## 거리가 최소인 물고기를 발견 (먹을 수 있는)
                        fish_r, fish_c, fish_dis = nr, nc, dis + 1
                    elif dis + 1 == fish_dis:  ## 거리가 같은 물고기를 발견
                        if (nr < fish_r) or (fish_r == nr and nc < fish_c):
                            fish_r, fish_c, fish_dis = nr, nc, dis + 1

                else: continue


    return (fish_r, fish_c, fish_dis)


N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

eat = 0
sh_r, sh_c = 0, 0
sh_size = 2
res = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sh_r, sh_c = i, j
            arr[i][j] = 0
            break

while True:

    fish_r, fish_c, fish_dis = move_shark(sh_r, sh_c, [[0] * N for _ in range(N)])

    if fish_r == N and fish_c == N:
        break

    res += fish_dis
    fish_size = arr[fish_r][fish_c]
    eat += 1

    if sh_size == eat:  ## 먹은 물고기만큼 성장
        sh_size = eat + 1
        eat = 0

    sh_r, sh_c = fish_r, fish_c  ## 상어 위치 바꿔주기
    arr[fish_r][fish_c] = 0  ## 먹힌 물고기는 0으로 변환

print(res)









