import copy

def comb(n, r):
    global enemies

    if r == 0:
        # print('현재의 조합은', tr)
        soldiers = [(N, tr[0]), (N, tr[1]), (N, tr[2])]
        play_game(copy.deepcopy(enemies), soldiers)
        return
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

def play_game(enemies, soldiers):
    global max_cnt

    remove_count = 0  # 제거한 적의 수
    attack = [-1] * 3

    while enemies:
        # 3명의 궁수들의 위치에서 D 이하의 가장 가까운 병사를 찾는다.
        # print('시작한 while 문', enemies)
        for s_idx in range(3):
            min_dis = N * M
            for enemy in enemies:
                dis = abs(soldiers[s_idx][0] - enemy[0]) + abs(soldiers[s_idx][1] - enemy[1])  # 적과 병사 사이의 거리를 구한다./ 가장 가까운 적을 찾는 과정이다.
                if dis < min_dis and dis <= D:
                    min_dis = dis
                    attack[s_idx] = enemy

        # 공격할 적을 찾았다면 적 리스트에서 remove하기
        for s_idx in range(3):
            if attack[s_idx] != -1 and attack[s_idx] in enemies:
                # print(enemies)
                # print(soldiers[s_idx], attack[s_idx], s_idx)
                enemies.remove(attack[s_idx])
                remove_count += 1
                attack[s_idx] = -1    # 다음턴을 위해 돌려놓기

        ## 이제 3명의 병사에 대해서 각각 공격을 마쳤다.
        ## 즉, 턴이 끝났으므로 적들을 한 칸씩 앞으로 전진
        enemies = list(map(lambda x: (x[0] + 1, x[1]), enemies))
        # 성을 지나지 않은 적들만 다시 넣기
        enemies = [enemy for enemy in enemies if enemy[0] < N]
        # print('remove_count', remove_count)

    if max_cnt < remove_count:
        max_cnt = remove_count

    # print('이번 턴의 최고 제거수는', max_cnt)

##########################################################################
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
enemies = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemies.append((i, j))

enemies.sort(key=lambda x: x[1])        # 열 기준으로 정렬, 왼쪽에 있는 적들이 앞쪽에 배치
max_cnt = 0

an = [i for i in range(M)]      # 조합을 만들기 위한
tr = [0] * 3

comb(M, 3)
print(max_cnt)
