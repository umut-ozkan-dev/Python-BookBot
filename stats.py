def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def wordcount(text):
    words = text.split()
    print(f"Found {len(words)} total words")


def charcount(text):
    lower_text = text.lower()
    dictionary = {}
    for c in lower_text:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    dictionary

    return dictionary
