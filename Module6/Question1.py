"""
What is the output of the following Python code block? Explain the logic of the given code.
Explain the logic of the given program and write the output as well.

a=2
b=12
c=1
d=a<b>c-1
d=2<12>1-1
d=2<12>0
d=1>0
print(d)
"""



"""
Output: True
Output: True
Output: True
Output: True

"""

"""
Logic of the program:

First we have declared a = 2, b = 12, c = 1

We set d to a<b>c-1
This means:
    First c-1 is calculated since - has higher operator precedence.
    Now the condition is checked from left-to-right since all operators have same precedence


"""