
# 2*2 크기로 하나씩 끼워 맞춘다. 만약 1이 있으면 건너띄고 맞추기
# 인덱스 고려하기
# 인덱스 홀수번째 행에서는 만약 안채워진 칸이 있다면 고려해보고 채우기

for tc in range(1, int(input())+1):
    h, w = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(h)]
    block_cnt = 0

    for i in range(h-1):
        if h % 2 or (h % 2 == 0 and i % 2 == 0):
            if i % 2 == 0 or (i % 2==1 and arr[i].count(0)):
                for j in range(w-1):
                    if arr[i][j] or arr[i][j+1] or arr[i+1][j] or arr[i+1][j+1]:
                        # 하나라도 벽돌이 있다면
                        continue
                    else:   # 해당 위치에 하나도 벽돌이 없으면/ 2로 표시
                        if w % 2  or (w % 2 == 0 and j % 2 == 0):
                            block_cnt += 1
                            arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1] = block_cnt, block_cnt, block_cnt, block_cnt
                            continue # 다음 열은 고려할 필요가 없으므로

    print(f'#{tc} {block_cnt}')
    # for i in range(h):
    #     print(*arr[i])
    print('=======================================')

