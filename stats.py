import string


def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def wordcount(text):
    words = text.split()
    return len(words)


def calc_estimated_time(word_count):
    """Estimated the average adult reads  at a rate of 238 words per minute."""

    total_minutes = round(word_count / 238)
    total_hour = total_minutes // 60
    remaining_minutes = round((total_minutes - (total_hour * 60)))
    estimated_time = f"{round(total_hour)} hours and {remaining_minutes} minutes"
    return estimated_time


def charcount(text):
    lower_text = text.lower()
    dictionary = {}
    for c in lower_text:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    return dictionary


def print_report(bookpath, estimated_time, word_count, formatted_sorted_list):
    print("========Python-Bookbot========")
    print(f"Analysis for the book found in: {bookpath}")
    print("------------------------------")
    print(f"Word Count: {word_count}")
    print("------------------------------")
    print(f"Estimated time to read : {estimated_time}")
    print("------------------------------")
    print(f"Character Count:\n{ formatted_sorted_list }")
    print("=============END==============")


def sort_on(dict_tuple: tuple[str, int]) -> int:
    return dict_tuple[1]


def chars_dict_to_sorted_list(dictionary: dict[str, int]):
    emptly_list = []
    for key in dictionary.keys():
        if key in string.ascii_letters:
            emptly_list.append((key, dictionary[key]))

    return emptly_list


def format_sorted_list(sorted_list):
    string_word_count = ""
    for tuple in sorted_list:
        string_word_count += f"{tuple[0]} : {tuple[1]} \n"

    return string_word_count
