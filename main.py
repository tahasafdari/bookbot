import sys
from stats import get_num_words, get_num_chars, sort_char_counts

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    sorted_char_counts = sort_char_counts(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    for char_info in sorted_char_counts:
        if char_info['char'].isalpha():
             print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()