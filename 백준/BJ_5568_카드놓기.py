## 나이순으로 출력
## 나이가 같으면 가입한 순으로 출력

N = int(input())
people = []
ages = []
res = []

for i in range(N):
    age, name = input().split()
    age = int(age)
    people.append([age, name])
    ages.append(age)

ages.sort()
for i in range(len(ages)):
    if i != 0 and ages[i-1] == ages[i]:
        continue
    else:
        for j in range(len(people)):
            if ages[i] == people[j][0]:
                res.append(people[j])

for i in range(N):
    print(*res[i])

