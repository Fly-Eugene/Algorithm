
# 해당 색종이로 모두 가릴 수 있는지 체크하는 함수
def check(width, paper_cnt):
    start_c = wrongs[0][1]
    paper_cnt -= 1        # 시작 시점에 바로 색종이를 하나 쓰게됨

    for w_idx in range(1, len(wrongs)):
        if start_c + width < wrongs[w_idx][1]: # 현재 시작열 + 너비 가 다음 회색칸의 열보다 작으면 == 다음 회색칸을 가리지 못하면
            start_c = wrongs[w_idx][1]    # 새로운 색종이로 다음 회색칸을 덧댄다
            paper_cnt -= 1

            if paper_cnt < 0:
                return False

    return True


N, M = map(int, input().split())
cnt = int(input())

W = int(input())
wrongs = [list(map(int, input().split())) for _ in range(W)]
wrongs.sort(key = lambda x : x[1])

r_max = max(i[0] for i in wrongs)       # r_max는 최소 색종이 길이다 => 왜? 색종이는 무조건 밑변이 땅에 붙어있어서
c_max = max(i[1] for i in wrongs)       # c_max는 최대 색종이 길이다 => 옆으로 최대 길이니까??
res = c_max

while r_max <= c_max:

    mid = (r_max + c_max) // 2
    if check(mid-1, cnt):       ## 여기서 왕왕 주의!! 음,,, 우리가 생각하는 너비 -1 로 넣어줘야한다. 우리는 idx 값으로 가지고 있기 때문에, 현재 점 + 2칸 == 너비 3이 된다.
        c_max = mid - 1       # 색종이 길이 절반으로 줄여보기
        res = min(res, mid)
    else:
        r_max = mid + 1      # 색종이 길이 늘리기

print(res)

