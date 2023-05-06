"""
Write a Python Program to Check if a Given Key Exists in a Dictionary or Not.
"""
dict_ = {"1":1,"2":"2","3":3,"4":4}
key = (input())
try:
    print(key, "is in dict. And it's value is:",dict_[key])
except:
    print(key, "is not in dict")

