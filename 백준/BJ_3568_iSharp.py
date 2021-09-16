
string = list(input().split())


## 중간에는 , 없애고 끝에는 ; 없애기
for i in range(1, len(string)):
    string[i] = string[i][:-1]

kind = ['*', ']', '&', '[']
res = [string[0]] * (len(string) - 1)
var_name = [''] * (len(string) - 1)

for i in range(1, len(string)):
    for j in range(len(string[i])-1, -1, -1):
        if string[i][j] in kind:
            if string[i][j] == ']':
                res[i-1] += '[]'
            elif string[i][j] == '[':
                continue
            else:
                res[i-1] += string[i][j]
        else:
            var_name[i-1] = string[i][j] + var_name[i-1]


for i in range(len(res)):
    print(res[i] + ' ' + var_name[i] + ';')

