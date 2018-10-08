import string


def eCounter(text):
    newText = ""
    count = 0
    numofwords = 0
    for char in text:
        if char not in string.punctuation:
            newText += char
    newText = newText.split()
    for words in newText:
        numofwords += 1
        if words.find("e") != -1:
            count += 1
    print("Your text contains {0} words, of which {1} ({2}%) contain an 'e'.".format(str(numofwords), str(count),
                                                                                     str(count / numofwords * 100)))


text = '''Assign to a variable in your program a triple-quoted string that contains your favourite paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.
Write a function which removes all punctuation from the string, breaks the string into a list of words, and counts the number of words in your text that contain the letter “e”. Your program should print an analysis of the text like this:'''
eCounter(text)
