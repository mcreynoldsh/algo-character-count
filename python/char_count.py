from functools import cmp_to_key
from operator import le


def char_count(str):
  unique_chars = []
  str= str.lower()
  char_list =sorted(str)
  count_list = []
  
  
  def sort_by_num(a,b):
    if a[1] - b[1] > 0:
      return -1
    elif a[1] - b[1] < 0:
      return 1
    elif a[1] == b[1] and a[0] < b[0]:
      return -1
    elif a[1] == b[1] and a[0] > b[0]:
      return 1
    else:
      return 0  

  
  for x in char_list:
    if unique_chars.count(x) == 0 and x.isalpha():
      unique_chars.append(x)
  
  for letter in unique_chars:
    count_list.append([letter, char_list.count(letter)])
  
  return sorted(count_list, key= cmp_to_key(sort_by_num)) 

