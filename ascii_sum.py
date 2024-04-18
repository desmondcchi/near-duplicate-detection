def ascii_sum(text: str) -> int:
  sum = 0
  for c in text:
    sum += ord(c)
  
  return sum

def dec_to_bin(num: int) -> str:
  """
  Converts decimal number into 8-bit binary string (num <= 256).
  """
  binary_str = bin(num)
   
  res = ""

  for i in reversed(range(len(binary_str))):
    if binary_str[i] == "b" or i == len(binary_str) - 1 - 8:
      break

    res += binary_str[i]
  
  while len(res) != 8:
    res += "0"
  
  return res[::-1]

# while True:
#   text = input("Input: ")
#   a_sum = ascii_sum(text)
#   hashed_sum = a_sum % 256

#   print(format(1, "#04b"))
#   print(f"Ascii Sum: {a_sum}")
#   print(f"Hashed Sum: {hashed_sum}")
#   print(f"Binary String: {dec_to_bin(hashed_sum)}")
