from stats import wordcount, get_book_test, charcount, print_report

filepath = "books/frankenstein.txt"


def main():
    """ The main function """
    text = get_book_test(filepath)
    word_count = wordcount(text)
    # print(charcount(text))
    print_report(filepath, word_count)


main()
