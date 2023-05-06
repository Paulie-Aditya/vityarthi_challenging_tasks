"""
Mr. Ashok Goel has spent ‘n’ units of effort in preparing for UPSC examination in a year.
Can you calculate using a Python program how many hours, minutes and seconds he has
spent on attaining success.
"""

n = int(input())

hours = n//3600
minutes = (n%3600 )//60
seconds = ((n%3600)%60)

print("Hours: ",hours, end = "\n")
print("Minutes: ",minutes, end = "\n")
print("Seconds: ",seconds, end = "\n")

