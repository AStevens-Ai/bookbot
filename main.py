def main() :
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_word_count(text)
    count_of_char = get_char_count(text)
    sorted_counts = sort_counts(count_of_char)
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document")
    for char, count in sorted_counts:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
       

def get_word_count(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_count(text):
    count_dict = {}
    my_string = text
    low_case_string = my_string.lower()
    character = list(low_case_string)
    for char in character:
        if char not in count_dict:
            count_dict[char] = 1
        elif char in count_dict:
            count_dict[char] += 1
    return count_dict

def sort_counts(dict):
    sorted_counts = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts
    
main()