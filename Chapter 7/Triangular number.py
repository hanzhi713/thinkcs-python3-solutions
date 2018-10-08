def print_triangular_number(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
        print(str(i) + "       " + str(sum))


print_triangular_number(5)
