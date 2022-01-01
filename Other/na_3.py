
def palindrome(a, b):
    words = [a+b, b+a]
    palin = [1, 1]

    for word in words:
        for i in range(len(word)//2):
            if word[i] == word[len(word)-1-i]:
                continue
            else:
                idx = words.index(word)
                palin[idx] = 0
                break

    if palin.count(0) == 2:
        return False
    else:
        return True



def comb(i, j, P, pair, N):
    global sel, A

    if i == 2:
        print('----------------------')
        print(sel)
        print(P)
        if palindrome(P[sel[0]], P[sel[1]]):
            new_P = []
            for i in range(N):
                if i not in sel:
                    new_P.append(P[i])
            pair.append(sel)

            if new_P == []:
                print('지금 정답이야 !!!!!!!!!!')
                for p in pair:
                    if 1 in p:
                        idx = p.remove(1)
                        print(P[p[0]])
                        A.append(P[idx[0]])
            else:
                comb(0, 0, new_P, pair, len(new_P))

    else:
        for k in range(j, N-2+i+1):
            sel[i] = k
            comb(i+1, j+1, P, pair, N)


P = ["11","111","11","211"]
N = len(P)
sel = [0] * 2
comb(0, 0, P, [], N)
A = []


print(A)