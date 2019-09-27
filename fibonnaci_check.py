#check if the following number is fibonacci or not
import sys
import math

num = int(input("Please enter a number: "))

#make sure the number is positive
if(num < 0):
	print("Numeber should be positive")
	sys.exit(1)

#check if entered number is perfect square
def PerfectSquareCheck(n):
	c = math.sqrt(n)
	if(c*c == n):
		return 0
	elif(c*c != n):
		return 1

#print(PerfectSquareCheck(num))


flag1 = PerfectSquareCheck((5*(num*num)) + 4)
flag2 = PerfectSquareCheck((5*(num*num)) - 4)

#print(flag1)
#print(flag2)

if(flag1 == 0 or flag2 == 0):
	print("{0} is a fibonnaci number".format(num))
else:
	print("{0} is not a fibonnaci number".format(num))
	
