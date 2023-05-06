"""
A quiz was conducted in a programming tutorial class for 10 marks. Calculate Mean and
Standard Deviation of the marks scored by minimum seven students in the class. Use the
appropriate functions provided by Python.
"""

scores = list(map(int,input("Enter 7 integers with spaces: "),split()))

mean = round((sum(scores) / len(scores)),3)

