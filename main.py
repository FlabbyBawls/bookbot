from stats import get_num_words
from stats import get_character_count
from stats import get_sorted_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]
    entire_book = get_book_text(path_to_book)
    word_count = get_num_words(entire_book)
    character_count = get_character_count(entire_book)
    sorted_list = get_sorted_chars(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("--------- Character Count -------")
    for c in sorted_list:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

def get_book_text(path_to_book):
    with open(path_to_book) as b:
        book_contents = b.read()
        return book_contents

main()
