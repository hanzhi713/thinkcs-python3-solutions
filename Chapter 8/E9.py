def remove_letter(char, text):
    charremovedText = ""
    for letter in text:
        if letter != char:
            charremovedText += letter
    return charremovedText


print(remove_letter("a", "banana"))
