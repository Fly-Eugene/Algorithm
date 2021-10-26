
dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]
dir_idx = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

king, stone, N = input().split()
ord("A") ## 65

## 8행 == 0행, 1행 == 7행
## A열 == ord("A") - 65 == 0열
## H열 == 7열

king_r = 8 - int(king[1])
king_c = ord(king[0]) - 65

stone_r = 8 - int(stone[1])
stone_c = ord(stone[0]) - 65


for i in range(int(N)):
    dir = input()
    idx = dir_idx.index(dir)

    king_nr = king_r + dr[idx]
    king_nc = king_c + dc[idx]

    ## 인덱스 체크
    if 0 <= king_nr < 8 and 0 <= king_nc < 8:
        # 스톤이랑 겹칠 때
        if king_nr == stone_r and king_nc == stone_c:
            stone_nr = stone_r + dr[idx]
            stone_nc = stone_c + dc[idx]

            # 스톤 인덱스 체크
            if 0 <= stone_nr < 8 and 0 <= stone_nc < 8:
                stone_r, stone_c = stone_nr, stone_nc
                king_r, king_c = king_nr, king_nc

        # 스톤이랑 겹치지 않을 때
        else:
            king_r, king_c = king_nr, king_nc

print(chr(king_c + 65) + str(8 - king_r))
print(chr(stone_c + 65) + str(8 - stone_r))
