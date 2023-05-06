def divisible_by_5(x:int):
    return x%5 == 0

number = int(input())
if divisible_by_5(number):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")