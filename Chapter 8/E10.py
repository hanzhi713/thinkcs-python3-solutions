def reverse(text):
    reversedText = ""
    for i in range(len(text) - 1, -1, -1):
        reversedText += text[i]
    return reversedText


def is_palindrome(suspectedword):
    if suspectedword == reverse(suspectedword):
        return True


print(is_palindrome("dad"))
