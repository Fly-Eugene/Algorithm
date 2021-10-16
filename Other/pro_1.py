
def N_to_N1(new_id):
    idx = 0
    N1_id = ''
    for ch in new_id:
        if ch in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            break
        else:
            idx += 1

    if idx == len(new_id):
        N1_id = new_id + '1'
        return N1_id
    else:
        S = new_id[:idx]
        N = new_id[idx:]
        print(S, N)
        N1_int = int(N) + 1
        N1_id = S + str(N1_int)
        return N1_id



registered_list = ["bird99", "bird98", "bird101", "gotoxy"]
new_id = "bird98"

answer = ''
while True:
    if new_id in registered_list:
        new_id = N_to_N1(new_id)
    else:
        answer = new_id
        break

print(answer)




