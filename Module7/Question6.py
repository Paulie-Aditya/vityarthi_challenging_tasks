"""
Python Program to remove the given key from a dictionary
"""

dict_ = {"1":1,"2":"2","3":3,"4":4}
key = (input())
try:
    del dict_[key]
    print("Removed")
    print("Updated dict:", dict_)
except:
    print(key, "is not in dict")