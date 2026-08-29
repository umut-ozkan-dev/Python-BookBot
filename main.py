from stats import (
    wordcount,
    get_book_test,
    charcount,
    print_report,
    chars_dict_to_sorted_list,
    sort_on,
    format_sorted_list,
    calc_estimated_time,
)

filepath = "books/frankenstein.txt"


def main():
    """The main function"""
    text = get_book_test(filepath)
    word_count = wordcount(text)
    estimated_time = calc_estimated_time(word_count)
    charcount(text)
    new_list = chars_dict_to_sorted_list(charcount(text))
    sorted_list = sorted(new_list, reverse=True, key=sort_on)
    formatted_sorted_list = format_sorted_list(sorted_list)

    print_report(filepath, estimated_time, word_count, formatted_sorted_list)


main()
