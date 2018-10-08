def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            return False
    return flag


print(is_prime(95869))
