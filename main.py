
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_letters(file_contents):
    lowered_string = file_contents.lower()
    freq = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for c in letters:
        freq[c] = lowered_string.count(c)
    return freq

def sort_on(dict):
    return dict["count"]

def sort_dict(letters_dict):
    letters_array = []
    for letter in letters_dict:
        letters_array.append({"letter": letter, "count": letters_dict[letter]})
    letters_array.sort(reverse=True, key=sort_on)
    return letters_array
    
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    letters_dict = count_letters(file_contents)
    for entry in sort_dict(letters_dict):
        print(f"The '{entry["letter"]}' character was found {entry["count"]} times")
    print("--- End report ---")