
def perm(idx):
    if idx == k:
        res.add(''.join(sel))
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                sel[idx] = cards[i]
                visited[i] = 1
                perm(idx+1)

                visited[i] = 0


n = int(input())
k = int(input())
cards = []
res = set()

for i in range(n):
    cards.append(input())

sel = [0]*k
visited = [0]*n

perm(0)
print(len(res))
