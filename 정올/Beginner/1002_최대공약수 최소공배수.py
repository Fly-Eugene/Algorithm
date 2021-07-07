
def find_div(num1, num2):
    for i in range(num1, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i

def find_mul(num1, num2):
    return (num1 * num2) // find_div(num1, num2)

N = int(input())
num_list = list(map(int, input().split()))

max_div = find_div(num_list[0], num_list[1])
min_mul = find_mul(num_list[0], num_list[1])

for i in range(2, N):
    max_div = find_div(max_div, num_list[i])
    min_mul = find_mul(min_mul, num_list[i])

print(max_div, min_mul)
