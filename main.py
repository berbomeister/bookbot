from stats import count_words,count_chars,report
import sys
def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # path = "./books/frankenstein.txt"
    path = sys.argv[1]
    fr = get_book_text(path)
    word_count = count_words(fr)
    char_counts = report(count_chars(fr))
    # print(f"{count_words(fr)} words found in the document")
    # print(count_chars(fr))
    # print(char_counts)
    output = f"""
============ BOOKBOT ============
Analyzing book found at {path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
    """
    print(output)
    for d in char_counts:
        print(f"{d['char']}: {d['num']}")
main()
