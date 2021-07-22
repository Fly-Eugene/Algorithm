from collections import deque


def bfs(time, cnt, board_cnt):
    queue = deque()
    queue.append((time, cnt, board_cnt))
    sticker_time[cnt] = time

    while queue:
        time, cnt, board_cnt = queue.popleft()
        # print(time, cnt)
        if cnt == S:
            break

        # board_cnt = cnt
        queue.append((time+1, cnt, cnt))

        if board_cnt:
            n_cnt = cnt + board_cnt
            if sticker_time[n_cnt] == -1:
                sticker_time[n_cnt] = time + 1
                queue.append((time+1, n_cnt, board_cnt))

        if cnt > 1 and sticker_time[cnt-1] == -1:
            sticker_time[cnt-1] = time + 1
            queue.append((time+1, cnt-1, board_cnt))

S = int(input())
sticker_time = [-1] * 1000
# clip_board = [0] * 10000

bfs(0, 1, 0)
print(sticker_time[S])

