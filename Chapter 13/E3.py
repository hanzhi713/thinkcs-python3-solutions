reader = open("test2.txt", "r")
counter = 0
linelist = []
while 1:
    counter += 1
    tempstr = reader.readline()
    if len(tempstr) == 0:
        break
    firstdigit = counter // 1000
    seconddigit = (counter - firstdigit * 1000) // 100
    thirddigit = (counter - firstdigit * 1000 - seconddigit * 100) // 10
    forthdigit = (counter - firstdigit * 1000 - seconddigit * 100 - thirddigit * 10)
    numberingdigits = "{0}{1}{2}{3} ".format(str(firstdigit), str(seconddigit), str(thirddigit), str(forthdigit))
    linelist.append(numberingdigits + tempstr)
reader.close()

writer = open("test2.txt", "w")
for line in linelist:
    writer.write(line)
writer.close()
