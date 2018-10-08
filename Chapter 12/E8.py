import string
from unit_tester import test


def cleanword(text, ifaddspace=False):
    cleaned = ""
    for let in text:
        if let not in string.punctuation:
            cleaned += let
        else:
            if ifaddspace == True:
                cleaned += " "
    return cleaned


def has_dashdash(text):
    if text.find("--") > -1:
        return True
    else:
        return False


def extract_words(text):
    cleaned = cleanword(text, True)
    cleaned = cleaned.lower()
    return cleaned.split()


def wordcount(word, text):
    count = 0
    for wd in text:
        if wd == word:
            count += 1
    return count


def wordset(text):
    result = []
    for i in text:
        if not i in result:
            result.append(i)
    result.sort()
    return result


def longestword(words):
    tempnum = 0
    for word in words:
        if len(word) > tempnum:
            tempnum = len(word)
    return tempnum


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time!  'Now', is the time? Yes, now.") ==
     ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==
     ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy'])

test(wordcount("now", ["now", "is", "time", "is", "now", "is", "is"]) == 2)
test(wordcount("is", ["now", "is", "time", "is", "now", "the", "is"]) == 3)
test(wordcount("time", ["now", "is", "time", "is", "now", "is", "is"]) == 1)
test(wordcount("frog", ["now", "is", "time", "is", "now", "is", "is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==
     ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) ==
     ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==
     ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this", "supercalifragilisticexpialidocious"]) == 34)
test(longestword([]) == 0)
