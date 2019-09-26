#Porgram to calculate simple intrest

#take input from the user 
P = input("Principle ammout = ")
R = input("Time = ")
T = input("Rate of Intrest = ")

#output of the program
output = (int(P)*int(R)*int(T))/100

#print output
print("Simple intrest on {0} is {1}".format(P, output))
