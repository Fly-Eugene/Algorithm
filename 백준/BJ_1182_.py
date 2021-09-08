def powerset(idx):
    global cnt

    if idx == n:
        res = 0
        if sel.count(0) != n:
            for i in range(n):
                if sel[i] == 1:
                    res += nums[i]
            if res == s:
                cnt += 1
        return
    else:
        sel[idx] = 1
        powerset(idx + 1)

        sel[idx] = 0
        powerset(idx + 1)


n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

sel = [0] * n
powerset(0)
print(cnt)