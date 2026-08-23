import stats

filepath = "books/frankenstein.txt"


def main():
    file_contents = stats.get_book_test(filepath)
    print(file_contents)


stats.wordcount(filepath)

main()
