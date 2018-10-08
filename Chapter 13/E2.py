reader = open("test.txt", "r")
while 1:
    tempstr = reader.readline()
    if tempstr.find("snake") > -1:
        continue
    if len(tempstr) == 0:
        break
    print(tempstr)
reader.close()
