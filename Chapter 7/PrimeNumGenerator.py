def PriNumGenerator(upperlimit):
    Plist = [2]
    num = 2
    print(2, end=", ")
    for num in range(2, upperlimit + 1):
        isprime = True
        for i in Plist:
            if num % i == 0:
                isprime = False
                break
        if isprime == True:
            Plist.append(num)
            print(num, end=", ")


PriNumGenerator(10000)
