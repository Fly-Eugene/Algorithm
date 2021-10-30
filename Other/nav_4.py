dr = [0, 1]
dc = [1, 0]

def bfs(r, c, score):

    queue = [(r, c, score)]

    while queue:
        now_r, now_c, now_score = queue.pop(0)

        for i in range(2):
            nr, nc = now_r + dr[i], now_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:  ## 인덱스 검사
                n_score = now_score + board[nr][nc]

                if board[nr][nc] == 0 and n_score < 0:  ## 현재 위치0, 음수인 상태
                    n_score *= -1

                if board_max[nr][nc] < n_score:
                    board_max[nr][nc] = n_score
                    queue.append((nr, nc, n_score))


board = [[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]]

N = len(board)
minus_INF = -10000 * N
board_max = [[minus_INF] * N for _ in range(N)]

bfs(0, 0, board[0][0])
answer = board_max[N-1][N-1]

print()





