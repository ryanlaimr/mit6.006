"""
Lecture 2:
Document Distance
-----------------
This iteration makes the algorithm for splitting the document into
a list of words more efficient.

"""


from get_documents import get_documents
import math
import string


translation_table = string.maketrans(
    string.punctuation + string.uppercase,
    " " * len(string.punctuation) + string.lowercase
)


def get_words_from_text(text):
  """
  Split a string into a list of words.

  """
  text = text.encode('utf-8')
  text = text.translate(translation_table)
  word_list = text.split()
  return word_list


def count_frequency(word_list):
  """
  Count the frequency of each word in the list
  by scanning the list of already encountered
  words.

  """
  D = dict()
  for new_word in word_list:
    if new_word in D:
      D[new_word] = D[new_word] + 1
    else:
      D[new_word] = 1
  return D


def word_frequencies_for_file(line_list):
  """
  Transform the document into a frequency map
  for each term.

  """
  word_list = get_words_from_text(' '.join(line_list))
  freq_map = count_frequency(word_list)
  return freq_map


def inner_product(D1, D2):
  """
  Take the inner product of the frequency maps.

  """
  result = 0.
  for key in D1:
    if key in D2:
      result += D1[key] * D2[key]
  return result


def vector_angle(D1, D2):
  """
  Compute the angle between two frequency vectors.

  """
  numerator = inner_product(D1, D2)
  denominator = math.sqrt(inner_product(D1, D1) * inner_product(D2, D2))
  return math.acos(numerator / denominator)


def main():
  """
  Compute the document distance.

  """
  (doc1, doc2) = get_documents()
  freq_map1 = word_frequencies_for_file(doc1)
  freq_map2 = word_frequencies_for_file(doc2)
  distance = vector_angle(freq_map1, freq_map2)
  print 'The distance between the documents is %0.6f (radians)' % distance
