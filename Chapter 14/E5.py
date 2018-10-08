import random
from unit_tester import test

my_tickets = [[7, 17, 37, 19, 23, 43], [7, 2, 13, 41, 31, 43], [2, 5, 7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]


def lotto_draw():
    lotto_generator = random.Random()
    result = []
    for i in range(6):
        result.append(lotto_generator.uniform(1, 50))
    return result


def lotto_match(lotto1, lotto2):
    count = 0
    for item in lotto1:
        if item in lotto2:
            count += 1
    return count


def lotto_matches(lotto, mytick):
    result = []
    for i in range(4):
        result.append(lotto_match(lotto, my_tickets[i]))
    return result


def PriNumGenerator(upperlimit):
    Plist = [2]
    for num in range(2, upperlimit + 1):
        isprime = True
        for i in Plist:
            if num % i == 0:
                isprime = False
                break
        if isprime == True:
            Plist.append(num)
    return Plist


def primes_in(l):
    prime_list = PriNumGenerator(50)
    count = 0
    for item in l:
        if item in prime_list:
            count += 1
    return count


def prime_misses(l):
    prime_list = PriNumGenerator(50)
    result = []
    new = []
    for i in range(len(l)):
        new += l[i]
    for item in prime_list:
        if item in new:
            continue
        else:
            result.append(item)
    return result


test(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)
test(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets) == [1, 2, 3, 1])
test(primes_in([42, 4, 7, 11, 1, 13]) == 3)
test(prime_misses(my_tickets) == [3, 29, 47])
