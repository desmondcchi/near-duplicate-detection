from helpers import ascii_sum, dec_to_bin
while True:
  text = input("Input: ")
  a_sum = ascii_sum(text)
  hashed_sum = a_sum % 256

  print(format(1, "#04b"))
  print(f"Ascii Sum: {a_sum}")
  print(f"Hashed Sum: {hashed_sum}")
  print(f"Binary String: {dec_to_bin(hashed_sum)}")
