def readposint():
    while True:
        try:
            a = int(input("Please enter a positive integer: "))
            if a <= 0:
                print("Non-positive integers are not allowed")
            else:
                break
        except ValueError as e:
            print(e)


print("The positive integer you entered is", readposint())
