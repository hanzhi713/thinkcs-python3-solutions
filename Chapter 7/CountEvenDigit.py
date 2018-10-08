def num_digits(n):
    count = 0
    while not -1 <= n <= 0:
        digit = n % 10
        if digit in [2, 4, 6, 8, 0]:
            count = count + 1
        n = n // 10
    return count


print(num_digits(345678935))
