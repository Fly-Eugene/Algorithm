
n1 = int(input())
n2 = int(input())
n3 = int(input())

mul_str = str(n1*n2*n3)

cnt_list = [0]*10

for item in mul_str:
    cnt_list[int(item)] += 1

for cnt in cnt_list:
    print(cnt)