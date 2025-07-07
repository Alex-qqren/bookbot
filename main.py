from stats import get_num_words
from stats import count_letters
from stats import log_report
import sys

def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  
  return file_contents


def main():
    # file_contents = get_book_text(sys.argv[1])

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # Exit with a non-zero status code indicating an error

    try:
        file_contents = get_book_text(sys.argv[1])
    except FileNotFoundError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # print(get_num_words(file_contents))
    # print(count_letters(file_contents))
    letter_dict = count_letters(file_contents)
    # print(log_report(letter_dict))
    dict_list = log_report(letter_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print(f"--------- Character Count -------")
    for dic in dict_list:
      print(f"{dic['char']}: {dic['num']}")
    print(f"============= END ===============")

main()