
N = int(input())
num_list = list(map(int, input().split()))
M = int(input())

div_sum = 0
mul_sum = 0

for i in range(N):
    if M % num_list[i] == 0:
        div_sum += num_list[i]
    if num_list[i] % M == 0:
        mul_sum += num_list[i]

print(div_sum)
print(mul_sum)

