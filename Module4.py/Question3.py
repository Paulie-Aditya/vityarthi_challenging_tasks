"""
A car has travelled D kilometers in T hours of time. What is the speed of the car in km/hr?
Write a python program to demonstrate.
"""

print("Enter integers for distance and time: ", end = "\n")

distance = int(input())
time = int(input())

speed = round((distance/time),3)

print("The speed of the car in km/hr is: ", speed)