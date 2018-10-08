def reverse(text):
    reversedText = ""
    for i in range(len(text) - 1, -1, -1):
        reversedText += text[i]
    return reversedText


def mirror(text):
    mirroredText = text + reverse(text)
    return mirroredText


print(mirror("Python"))
