def main() :
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_word_count(text)
    count_of_char = get_char_count(text)
    print(f"{count_of_char}")
       

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


main()