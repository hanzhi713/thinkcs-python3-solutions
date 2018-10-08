def count_occur(stri, subs):
    result = -len(subs)
    count = 0
    while 1:
        result = stri.find(subs, result + len(subs))
        if result == -1:
            break
        count += 1
    return count


print(count_occur("okokkookkasdkok", "ok"))
