
N = int(input())
screen = [0] * 100
buffer = 1

for i in range(6):
    screen[i] = i+1

for i in range(6, 100):
    screen[i] = max(screen[i-3]*2, screen[i-4]*3, screen[i-5]*4)

print(screen[N-1])

