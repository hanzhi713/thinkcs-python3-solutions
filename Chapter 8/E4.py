def count_letters(stri, char):
    result = -1
    count = 0
    while 1:
        result = stri.find(char, result + 1)
        if result == -1:
            break
        count += 1
    return count


print(count_letters("aacbasbaab", "a"))
