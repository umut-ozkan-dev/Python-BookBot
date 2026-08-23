def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def wordcount(filepath):
    text = get_book_test(filepath)
    words = text.split()
    print(f"Found {len(words)} total words")
