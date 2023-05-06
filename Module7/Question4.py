"""
A quiz was conducted in a programming tutorial class for 10 marks. Calculate Mean and
Standard Deviation of the marks scored by minimum seven students in the class. Use the
appropriate functions provided by Python.
"""
import math

scores = list(map(int,input("Enter 7 integers with spaces: "),split()))

mean = round((sum(scores) / len(scores)),3)

summation = 0
for score in scores:
    summation+=(abs(score-mean))**2

standard_deviation = math.sqrt(summation/len(scores))

print("Mean is:", mean)
print("Standard Deviation is:", standard_deviation)
