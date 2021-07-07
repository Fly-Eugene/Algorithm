import math

n1, n2 = map(int, input().split())

div_list = []

for i in range(1, int(math.sqrt(n1))+1):
    if n1 % i == 0:
        div_list.append(i)

        if n1 // i != i:
            div_list.append(n1 // i)

div_list.sort()

max_div = 1
for idx in range(len(div_list)-1, -1, -1):
    if n2 % div_list[idx] == 0:
        max_div = div_list[idx]
        break

min_mul = (n1//max_div) * (n2//max_div) * max_div

print(max_div)
print(min_mul)
