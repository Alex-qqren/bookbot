def get_num_words(book_text):
  num_words = len(book_text.split())
  return f"{num_words} words found in the document"

def count_letters(book_text):
  letter_dict = {}
  for char in book_text:
    lower_char = char.lower()
    if lower_char not in letter_dict:
      letter_dict[lower_char] = 1
    else:
      letter_dict[lower_char] += 1
  return letter_dict