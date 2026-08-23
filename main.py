filepath = "books/frankenstein.txt"

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


print(get_book_test(filepath))
