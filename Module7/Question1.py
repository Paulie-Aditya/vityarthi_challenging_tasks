"""
Asha has a huge collection of country currencies. She decided to count the total number of
distinct country currencies in her collection. She asked for your help. You pick the currency one
by one from a stack of country currencies.
Find the total number of distinct country currencies.

"""

n = int(input("Enter Number of Currencies: "))
countries= []
distinct = 0
for i in range(n):
    country = input("Enter name of country: ")
    if country in countries:
        print(distinct)
    else:
        distinct +=1
        print(distinct)
    countries.append(country)



