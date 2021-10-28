
def check_min_max(nx, ny):
    global min_x, min_y, max_x, max_y

    if nx < min_x:
        min_x = nx
    if nx > max_x:
        max_x = nx
    if ny < min_y:
        min_y = ny
    if ny > max_y:
        max_y = ny

move = {
    1 : [(0, 1), (0, -1)],
    2 : [(1, 0), (-1, 0)],
    3 : [(0, -1), (0, 1)],
    4 : [(-1, 0), (1, 0)]
}




T = int(input())

for tc in range(T):
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    x, y = 0, 0

    commands = list(input())  ## F, B, L, R
    now_dir = 1  ## 현재 바라보는 방향 (1, 2, 3, 4 = 북동남서)

    for command in commands:
        if command == 'F':
            dx, dy = move[now_dir][0]
            x, y = x + dx, y + dy
            check_min_max(x, y)

        elif command == 'B':
            dx, dy = move[now_dir][1]
            x, y = x + dx, y + dy
            check_min_max(x, y)

        elif command == 'L':
            if now_dir == 1:
                now_dir = 4
            else:
                now_dir -= 1

        elif command == 'R':
            if now_dir == 4:
                now_dir = 1
            else:
                now_dir += 1

    res = (max_x - min_x) * (max_y - min_y)
    print(res)




