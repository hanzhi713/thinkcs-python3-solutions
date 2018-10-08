def remove(text, target):
    cleanedText = ""
    index = text.find(target)
    cleanedText += text[:index] + text[index + len(target):]
    return cleanedText


print(remove("banabana", "ana"))
