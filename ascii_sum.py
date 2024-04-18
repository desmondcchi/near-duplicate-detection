def ascii_sum(text: str) -> int:
  sum = 0
  for c in text:
    sum += ord(c)
  
  return sum

while True:
  text = input("Input: ")
  a_sum = ascii_sum(text)
  hashed_sum = a_sum % 256

  print(format(1, "#04b"))
  print(f"Ascii Sum: {a_sum}")
  print(f"Hashed Sum: {hashed_sum}")
  print(f"Binary String: {format(hashed_sum, "#08b")}")
