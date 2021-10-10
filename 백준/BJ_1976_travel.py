
def Find(x):
    if p[x] == x:
        return x
    else:
        ## x의 부모를 찾고나서, x의 부모를 갱신해준다. !!
        parent = Find(p[x])
        p[x] = parent
        return parent

def Union(x, y):
    parent_x = Find(x)
    parent_y = Find(y)

    if parent_x == parent_y:
        return
    else:
        if parent_x < parent_y:
            p[parent_y] = parent_x
        else:
            p[parent_x] = parent_y



N = int(input())
M = int(input())

p = [i for i in range(N+1)]
for i in range(N):
    connect_list = list(map(int, input().split()))
    for j in range(N):
        if connect_list[j] == 1:
            Union(i+1, j+1)

res = "YES"
travel = list(map(int, input().split()))
for i in range(M-1):
    if p[travel[i]] == p[travel[i+1]]:
        continue
    else:
        res = "NO"
        break

print(res)




