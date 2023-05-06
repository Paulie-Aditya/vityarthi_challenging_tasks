def even(x:int):
    return x%2 == 0
number = int(input("a: "))

if even(number):
    print("The number is even")
else:
    print("The number is odd")
