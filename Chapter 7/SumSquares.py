def sum_of_squares(xs):
    sum = 0
    for i in xs:
        sum += i ** 2
    return sum


print(sum_of_squares([2, 3, 4]))
