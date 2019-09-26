#Program to calculate Compount Intrest

#take input
P = float(input("Principle Ammount = "))
R = float(input("Rate of Intrest = "))
T = float(input("Time = "))

#apply compound intrest formula
CT = P*pow((1 + R/100), T)

print("Compund Intrest on {0} is {1}".format(P, CT))

