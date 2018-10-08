def count_letters(stri, char):
    count = 0
    for l in stri:
        if l == char:
            count += 1
    print(count)


count_letters("aabaab", "a")
