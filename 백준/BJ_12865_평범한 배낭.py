
n, k = map(int, input().split())
objects = []

for _ in range(n):
    objects.append(list(map(int, input().split())))

arr = [0] * (k+1)
objects.sort(key = lambda x : x[0], reverse=True)

for ob in objects:
    w, v = ob
    if w < k+1:
        # 만약, 현재 무게가 이미 기록되 있다면 (동일 무게에 대해 가치가 다른 것을 고려)
        if arr[w] != 0:

            # 뒤 인덱스부터 현재 weight 까지 뒤로 돈다
            for idx in range(k, w-1, -1):
                if arr[idx] != 0:
                    if idx + w < k+1:  # 인덱스 오류 방지 막으려고
                        arr[idx+w] = max(arr[idx+w], arr[idx] + v)

            # 현재 위치 무게값 갱신
            arr[w] = max(arr[w], v)

        # 만약, 새로운 무게라면
        else:
            arr[w] = v
            # 위의 for문 똑같이 다시 쓴 것,..(낭비)
            for idx in range(k, w, -1):
                if arr[idx] != 0:
                    if idx + w < k+1:
                        arr[idx+w] = max(arr[idx+w], arr[idx] + v)

# print(arr)
print(max(arr))

