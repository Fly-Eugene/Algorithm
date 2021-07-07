# 0.5초 단위의 2차원 배열을 만든다
# 각 원소의 시작점부터 이동방향의 끝까지 해당 원소가 몇초에 위치하는지 표시한다.
# 배열의 길이가 2 이상인 곳을 find & 위치한 시간이 같으면 => 따로 저장해서 시간 순서대로 정렬한다.
# 원자 리스트에 원자가 있는지 확인하고, 원자배열에서 제거한다.

move = {0:(-1, 0), 1:(1, 0), 2:(0, -1), 3:(0, 1)}


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[]*(2001) for _ in range(2001)]
    ball_list = []
    pop_power = 0

    for _ in range(N):
        i, j, dir, power = map(int, input().split())
        arr[i][j].append((dir, power))






