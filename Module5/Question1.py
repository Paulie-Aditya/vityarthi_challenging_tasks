"""
On what input of a and b this program will display “I win the game”? Find the value of a and b.

if (a & b >= 1) | (a^b <=1) :
    print("I win the game")
else:
    print("I lose the game")
"""


"""
There are various inputs for which we can 'Win the game'.
Few of such inputs are:

a = 2, b= 2
a = 2, b=3
a = 2, b=10
a = 100, b = 100
"""

a = 100
b = 100
if (a & b >= 1) | (a^b <=1) :
    print("I win the game")
else:
    print("I lose the game")



