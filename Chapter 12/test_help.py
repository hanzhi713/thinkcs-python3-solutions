import string


def extract_words(text):
    cleaned = cleanword(text)
    cleaned = cleaned.lower()
    return cleaned.split()


def cleanword(text):
    cleaned = ""
    for let in text:
        if let not in string.punctuation:
            cleaned += let
    return cleaned


print(extract_words("she tried to curtsey as she spoke--fancy"))
