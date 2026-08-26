def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def wordcount(text):
    words = text.split()
    return len(words)


def charcount(text):
    lower_text = text.lower()
    dictionary = {}
    for c in lower_text:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    return dictionary


def print_report(bookpath, word_count):
    print("========Python-Bookbot========")
    print(f"Analysis for the book found in: {bookpath}")
    print("------------------------------")
    print(f"Word Count: {word_count}")
    print("------------------------------")
    print(f"Character Count: { None }")  ## FIX THİS
    print("=============END==============")



