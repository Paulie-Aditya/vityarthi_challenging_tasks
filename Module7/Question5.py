n = int(input("Enter number of words: "))

names = []
for i in range(n):
    names.append(input("Enter Name: "))

max_length = 0
longest_word = ""

for t in range(n):
    if len(names[t])>max_length:
        max_length = len(names[t])
        longest_word = names[t]

print("The word with the longest length is:",longest_word)
