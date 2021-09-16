
ball = [11, 2, 9, 13, 24]
order = [9, 2, 13, 24, 11]

temp, res = [], []

for od in order:

    while True:
        chk = False
        for tp in temp:
            if tp == ball[0] or tp == ball[-1]:
                chk = True
                ball.remove(tp)
                temp.remove(tp)
                res.append(tp)

        if chk == False:
            break

    if od == ball[0] or od == ball[-1]:
        ball.remove(od)
        res.append(od)

    else:
        temp.append(od)




print(res)





