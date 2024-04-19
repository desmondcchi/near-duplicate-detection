from helpers import ascii_sum, dec_to_bin
from collections import Counter

def hash_word(word: str) -> str:
  asc_sum = ascii_sum(word)
  return dec_to_bin(asc_sum % 256)

doc_1 = input("Input document 1: ")
doc_2 = input("Input document 2: ")
print("")

doc_1_words = doc_1.split(" ")
doc_2_words = doc_2.split(" ")

# Count words.
doc_1_word_counter = Counter()
doc_2_word_counter = Counter()

for word in doc_1_words:
  doc_1_word_counter[word.lower()] += 1

for word in doc_2_words:
  doc_2_word_counter[word.lower()] += 1

print("Word counts in document 1:")
for k, v in doc_1_word_counter.items():
  print(f"{k} : {v}")
print("")

print("Word counts in document 2:")
for k, v in doc_2_word_counter.items():
  print(f"{k} : {v}")
print("")

# Hash words.
doc_1_hashed_words = {}
doc_2_hashed_words = {}

for word in doc_1_word_counter.keys():
  doc_1_hashed_words[word] = hash_word(word)

for word in doc_2_word_counter.keys():
  doc_2_hashed_words[word] = hash_word(word)

print("Hash values of words in document 1:")
for k, v in doc_1_hashed_words.items():
  print(f"{k} : {v}")
print("")

print("Hash values of words in document 2:")
for k, v in doc_2_hashed_words.items():
  print(f"{k} : {v}")
print("")

# Build weight vectors V.
V_1 = [None for _ in range(8)]
V_2 = [None for _ in range(8)] 

for i in range(8):
  weight_1 = 0
  weight_2 = 0

  for k, v in doc_1_hashed_words.items():
    if v[i] == "1":
      weight_1 += doc_1_word_counter[k]
    else:
      weight_1 -= doc_1_word_counter[k]

  V_1[i] = weight_1

  for k, v in doc_2_hashed_words.items():
    if v[i] == "1":
      weight_2 += doc_2_word_counter[k]
    else:
      weight_2 -= doc_1_word_counter[k]

  V_2[i] = weight_2

# Compute simhash vectors.
simhash_1 = [(1 if n > 0 else 0) for n in V_1]
simhash_2 = [(1 if n > 0 else 0) for n in V_2]

# Compute simhash distance.
simhash_distance = 0
for i in range(8):
  if simhash_1[i] != simhash_2[i]:
    simhash_distance += 1

print(f"Simhash of document 1: {simhash_1}")
print(f"Simhash of document 2: {simhash_2}")
print("")
print(f"Simhash Distance (Hamming distance): {simhash_distance}")
