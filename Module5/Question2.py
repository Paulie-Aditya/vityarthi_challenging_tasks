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

"""
Logic of the Program is as follows:

First, the first parenthesis is checked.
The condition of (a & b >=1) is checked.
If this is False, the second condition is checked too, since there is an OR operator between the conditions.
The condition of (a^b <=1) is now checked.

If both of these are False, the else statement is executed.
That is, "I lose the game" is printed

If either of these are True, the block of code inside the if statement is executed.
That is, "I win the game" is printed


"""

a = 100
b = 100
if (a & b >= 1) | (a^b <=1) :
    print("I win the game")
else:
    print("I lose the game")