def get_num_words(text):
    words = text.split()
    return len(words)

## funcion that returns the number of characters in a text converted to lowercase, use a dictionary of String -> int for example {'p': 6121, 'r': 20818, 'o': 25225, ...
def get_num_chars(text):
    char_count = {}
    for char in text.lower():  # convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

## add a function that takes the dictionary of characters and their counts and returns a sorted list of dictionaries
## e.g. {"char": "b", "num": 4868} use the .sorted() method
def sort_char_counts(char_count):
    sorted_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return [{"char": char, "num": count} for char, count in sorted_counts]
