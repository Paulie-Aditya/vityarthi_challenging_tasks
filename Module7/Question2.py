"""
A startup company named 'MY_Chat' having four employees names as Sunny, Ravi, Vijay and
Messi having the respected salaries are 25000,23000, 26000, and 30000.
"""

MY_Chat = {"Sunny": 25000,"Ravi": 23000,"Vijay": 26000,"Messi":30000}

name = input("Employee who resigned: ")

try:
    del MY_Chat[name]
except:
    "This employee is not a part of this company."

print(MY_Chat)