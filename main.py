from stats import (
    wordcount,
    get_book_test,
    charcount,
    print_report,
    chars_dict_to_sorted_list,
    sort_on,
)

filepath = "books/frankenstein.txt"


def main():
    """The main function"""
    text = get_book_test(filepath)
    word_count = wordcount(text)
    charcount(text)
    # print_report(filepath, word_count)
    new_list = chars_dict_to_sorted_list(charcount(text))
    sorted_list = sorted(new_list,reverse=True,key=sort_on)
    print(sorted_list)


main()
