def get_num_words(book_string):
    words = book_string.split()
    amount = len(words)
    return amount

def get_character_count(book_string):
    char_count = {}
    characters = list(book_string)
    for c in characters:
        char = c.lower()
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    del char_count[" "]
    return char_count

def sort_on(dict):
    return dict["num"]

def get_sorted_chars(char_dict):
    list_of_chars = []
    for c in char_dict:
        char = {"char" : c, "num" : char_dict[c]}
        list_of_chars.append(char)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
