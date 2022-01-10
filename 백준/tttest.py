
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations

arr = [i for i in range(1, 5)]

for l in combinations(arr, 2):
    print(l)

print('==================================')
for l in combinations_with_replacement(arr, 2):
    print(l)

print('==================================')
for i in permutations(arr, 2):
    print(i)


