#The hypotenuse is the longest side of a right angled triangle. Using Pythagoras’s theorem, calculate the third side and also the area of the right triangle.

import math

width = int(input("Enter Width of Triangle: "))
height = int(input("Enter Height of Triangle: "))

hypotenuse = round(math.sqrt(height**2 + width**2),3)

area = 0.5*height*width

print("The third of the triangle is ", hypotenuse)
print("Area of the right angled triangle is ", area)
