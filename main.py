from stats import get_num_words

def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  
  return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    get_num_words(file_contents)

main()