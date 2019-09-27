#create a fibonacci series number
#using recursion
import sys

#recursive function to find fibonaccis series 
def fibonacci(n):
	if(n == 1): #base case 1
		return 0 
	elif(n == 2): #base case 2
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Please eneter the numbe: "))

#make sure number is positive
if(num < 0):
	print("number needs to be positive")
	sys.exit(0)

#call to reccursive function
output = fibonacci(num)

print("The {0} fibonacci number in series is {1}".format(num, output))
