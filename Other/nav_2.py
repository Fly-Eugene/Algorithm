
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n = 5
jump = 3
answer = []

arr = [[0] * 5 for _ in range(5)]
arr[0][0] = 1

now_jump = 1  ## 현재까지 기록한 jump 수
now_move = 0  ## 현재까지 이동한 수

while True:
    dir_idx = 0
    r, c = 0, 0
    change_dir = n - 1  ## 몇 칸가고 방향을 바꿀 것인지

    while change_dir > 0:
        if change_dir == n - 1:
            repeat = 3
        else:
            repeat = 2

        for _ in range(repeat):
            for i in range(change_dir):
                dr, dc = dir[dir_idx]
                r, c = r + dr, c + dc

                if arr[r][c] == 0:
                    now_move += 1
                    if now_move % jump == 0:
                        now_jump += 1
                        arr[r][c] = now_jump
                        if now_jump == n ** 2:
                            answer = [r + 1, c + 1]

                else: continue

            if dir_idx == 3:
                dir_idx = 0
            else:
                dir_idx += 1

        change_dir -= 1  ## 같은 방향으로 가는 횟수 감소시킴

    if now_jump == n ** 2:
        break

    for i in range(n):
        print(arr[i])

    print('--------------------')

print(answer)



