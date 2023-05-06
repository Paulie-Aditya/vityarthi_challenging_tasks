#Profit calculation Using “Operators”

"""
Mr. Rama buys a 2BHK luxury apartment in Bhopal for the cost of Rs.A and he has gone for
interior decorations with Rs.B cost. Luckily in his territory the government has announced a
Special Economic Zone (SEZ). The demand for the flats in that area was boosted by the white
collar & golden collar professionals. If he sells the flat for Rs.Z, what is his profit in
percentage? Write a Python program to compute the profit in percentage?
"""

print("Enter Cost, Interior and Selling Price: ", end = " ")
cost,interior_price,selling_price =list(map(int,input().split()))

total_cost = (cost+interior_price)

profit = round((((selling_price - total_cost)/(total_cost)) * 100),3)

print("The profit is: ",profit)
