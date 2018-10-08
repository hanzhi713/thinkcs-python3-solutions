def sum_to(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


while 1:
    try:
        n = int(input("Sum up from 1 to n. Please enter the upperlimit n. n must be greater than 0"))
        if n > 0: break
    except:
        None
print(sum_to(n))
