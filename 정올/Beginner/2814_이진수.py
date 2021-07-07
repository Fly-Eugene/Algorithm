
num = input()
res = 0

for i in range(len(num)):
    res += int(num[i]) * (2**(len(num)-i-1))

print(res)



