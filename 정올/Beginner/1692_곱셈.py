
n1 = int(input())
n2 = int(input())

n2_str= str(n2)
res = 0
for i in range(2, -1, -1):
    res += (n1 * int(n2_str[i])) * (10**(2-i))
    print(n1 * int(n2_str[i]))

print(res)

