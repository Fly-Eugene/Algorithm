import fractions
from itertools import combinations

X = [1, 1, 2]
Y = [3, 2, 10**3 + 3]
N = len(X)

fraction_list = []
for i in range(N):
    fraction_list.append(fractions.Fraction(X[i], Y[i]))

print(fraction_list)
cnt = 0
for i in range(N):
    for comb in combinations(fraction_list, i):
        if sum(comb) == 1:
            cnt += 1

print(cnt)

