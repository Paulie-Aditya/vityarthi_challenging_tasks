a = int(input("a: "))
b = int(input("b: "))
a = a ^ b
b = a ^ b
a = a ^ b
print("a:",a,end="\n")
print("b:",b)