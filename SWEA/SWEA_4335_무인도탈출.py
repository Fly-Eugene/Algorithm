# N이 20이하 => 완전탐색
# 부분집합 => 순열 => 모든 박스를 쓰지 않아도 됨
# (가로, 세로), 높이 입력 받기
# =>(가로,높이), 세로 / (세로, 높이), 가로 도 설계해봐야 함

# def subset(idx):
#     if idx == N:
#         check = [0] * len(sub_res)
#         perm_res = [0] * len(sub_res)
#         # print('여기는 subset return', sub_res)
#         perm(0, check, perm_res)
#         return
#
#     sub_res.append(idx)
#     subset(idx+1)
#
#     sub_res.remove(idx)
#     subset(idx+1)

def perm(idx):

    if idx == N:
        box_topping(0, perm_res, [10000, 10000], 0)        # 무조건 10000 이하의 길이이므로 기본설정
        return
    else:
        for i in range(N):
            if check[i] == 0:
                perm_res[idx] = i
                check[i] = 1
                perm(idx + 1)

                check[i] = 0

def box_topping(idx, perm_res, pre_box ,height):
    global max_height
    global choose_bottom
    global boxes

    if idx == len(perm_res):
        if height > max_height:
            max_height = height
        return

    for i in range(3):
        m, n, h = choose_bottom[i]      # 그냥 밑면 인덱스 따로 저장하는 변수
        if (pre_box[0] >= boxes[perm_res[idx]][m] and pre_box[1] >= boxes[perm_res[idx]][n]) or (pre_box[0] >= boxes[perm_res[idx]][n] and pre_box[1] >= boxes[perm_res[idx]][m]):
            n_height = height + boxes[perm_res[idx]][h]
            if n_height > max_height:
                max_height = n_height
            box_topping(idx+1, perm_res, [boxes[perm_res[idx]][m], boxes[perm_res[idx]][n]], n_height)

        else:
            continue


for tc in range(1, int(input())+1):
    N = int(input())
    boxes = []
    for n in range(N):
        boxes.append(list(map(int, input().split())))

    # sub_res = []
    # subset(0)

    check = [0] * N
    perm_res = [0] * N
    max_height = 0
    choose_bottom = [(0,1,2), (0,2,1), (1,2,0)]   # 밑면을 가로세로 / 가로높이 / 세로높이로 지정한다는 뜻
    perm(0)

    print(f'#{tc} {max_height}')
