import math

N = int(input())
div_list = []

for i in range(1, int(math.sqrt(N+1))+1):
    if N % i == 0:
        div_list.append(i)

        if N // i != i:
            div_list.append(N // i)

print(*sorted(div_list))
