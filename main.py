def get_book_text(path_to_file):
  with open(path_to_file) as file:
    file_contents = file.read()
  
  return file_contents

def count_words(book_text):
  num_words = len(book_text.split())
  print(f"{num_words} words found in the document")



def main():
    file_contents = get_book_text("books/frankenstein.txt")
    count_words(file_contents)

main()