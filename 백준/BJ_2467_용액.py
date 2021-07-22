
N = int(input())
liquid_list = []
trans = -1
for i in range(N):
    num = int(input())
    if trans == -1 and num > 0:
        trans = i
    liquid_list.append(num)

min_sum = 0
comb = []
if abs(liquid_list[trans-1] + liquid_list[trans-2]) < abs(liquid_list[trans] + liquid_list[trans+1]):
    min_sum = abs(liquid_list[trans-1] + liquid_list[trans-2])
    comb = [trans-1, trans-2]
else:
    min_sum = abs(liquid_list[trans] + liquid_list[trans+1])
    comb = [trans, trans+1]

acid_left, acid_right = 0, trans - 1
kal_left, kal_right = trans, len(liquid_list) - 1

while acid_left <= acid_right and kal_left <= kal_right:
    pass



