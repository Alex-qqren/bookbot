def get_num_words(book_text):
  num_words = len(book_text.split())
  return num_words

def count_letters(book_text):
  letter_dict = {}
  for char in book_text:
    lower_char = char.lower()
    if lower_char not in letter_dict:
      letter_dict[lower_char] = 1
    else:
      letter_dict[lower_char] += 1
  return letter_dict

def log_report(obj):
  dict_list = []
  
  for key in obj:
    if key.isalpha():
      value = obj[key]
      dict_list.append({"char": key, "num": value})

  def sort_on(items):
    return items["num"]

  dict_list.sort(reverse = True, key=sort_on)
  
  return dict_list