
N = int(input())
screen = [0] * N
buffer = [0] * N

## 3번 누르는 것까지는 1번 버튼을 그냥 출력하는게 최대라서
screen[0] = 1

for i in range(1, N):
    a = screen[i-1] + 1
    b, c = 0, 0
    if 0 <= i-3:
        b = screen[i-3] + buffer[i-1]
    if 0 <= i-2:
        c = screen[i-1] + buffer[i-2]

    ## 경우는 3가지, a가 가장 큰 경우 / b가 a,c보다 같거나 큰경우/ c가 a, b 보다 큰 경우
    



