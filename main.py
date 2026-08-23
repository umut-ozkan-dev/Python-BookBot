from stats import wordcount, get_book_test, charcount

filepath = "books/frankenstein.txt"


def main():
    text = get_book_test(filepath)
    # wordcount(text)
    print(charcount(text))


main()
