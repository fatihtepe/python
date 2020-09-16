counts = [0] * 26

check = True
while check:
  word = input("Enter a string: ")
  word = word.lower()
  if word == "exit":
    check = False
  else:
    for ch in word:
      index = ord(ch) - ord("a")
      counts[index] += 1

maxCount = max(counts)

for i in range(len(counts)):
  if counts[i] == maxCount:
    index = i
    break

maxChar = chr(ord("a") + index)
print(maxChar, "->", maxCount)