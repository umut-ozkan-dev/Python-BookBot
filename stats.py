import string


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


def sort_on(dict_tuple: tuple[str, int]) -> int:
    return dict_tuple[1]


def chars_dict_to_sorted_list(dictionary: dict[str, int]):
    emptly_list = []
    for key in dictionary.keys():
        if key in string.ascii_letters:
                emptly_list.append((key,dictionary[key]))

    return emptly_list
