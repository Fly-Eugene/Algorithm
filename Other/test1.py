
boxes = [[1, 2], [2, 3], [3, 1]]
box_cnt = len(boxes)
pairs = []

for box in boxes:
    a, b = box

    if a in pairs:
        pairs.remove(a)
        box_cnt -= 1
    else:
        pairs.append(a)

    if b in pairs:
        pairs.remove(b)
        box_cnt -= 1
    else:
        pairs.append(b)

res = 0
if box_cnt < len(pairs):
    res = box_cnt
else:
    res = len(pairs)

print(res)



