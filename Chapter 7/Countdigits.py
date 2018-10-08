def num_digits(n):
    count = 0
    while not -1 <= n <= 0:
        count = count + 1
        n = n // 10
    return count


print(num_digits(-345))
