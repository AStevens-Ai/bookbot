def main() :
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_of_words = get_word_count(text)
    print(f"{num_of_words} words found in the document")
       

def get_word_count(text):
    words = text.split()
    return len(words)



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()