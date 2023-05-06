"""
School attendance register needs to be prepared with several columns. Amongst ‘Name’
column size need to be decided based on the longest word in the list of students’ names.
The program takes a list of words and returns the word with the longest length. If there
are two or more words of the same length then the first one is considered.

"""
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
