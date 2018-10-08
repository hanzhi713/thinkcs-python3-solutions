def remove(text, target):
    cleanedText = text
    while 1:
        index = cleanedText.find(target)
        if index == -1:
            break
        cleanedText = cleanedText[:index] + cleanedText[index + len(target):]
    return cleanedText


print(remove("banabanabanacana", "ana"))
