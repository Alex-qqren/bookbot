from stats import get_num_words
from stats import count_letters
from stats import log_report

def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  
  return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    # print(get_num_words(file_contents))
    # print(count_letters(file_contents))
    letter_dict = count_letters(file_contents)
    # print(log_report(letter_dict))
    dict_list = log_report(letter_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print(f"--------- Character Count -------")
    for dic in dict_list:
      print(f"{dic['char']}: {dic['num']}")
    print(f"============= END ===============")

main()