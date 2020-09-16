gallon = float(input("Enter amount of gallons: "))
liter = gallon * 3.7854
barrel = gallon / 19.5
cost = liter * 0.75

print(str(barrel) + " barrel(s) of oil required to produce " + str(gallon) + " gallon(s) of gas")
print("It wil cost " + str(cost) + " dollar(s)")