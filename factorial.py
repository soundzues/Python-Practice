#factorial of number
from functools import reduce

#defining function to multiply
def do_mult(x,y):
	return x*y

num = input("please add number you want to take factorial of = ")
#print(num1)

#change type to num
num = int(num)
fact = num

#intialize list
factoList = [num]

i = 0
while i < (num - 1):
	#print(i)
	fact = fact - 1
#	print(fact)	
	factoList.append(fact)
	i += 1 

#for x in range(len(factoList)):

#normal function:
#output = reduce(do_mult, factoList)

#Using Lamda function
output = reduce(lambda x,y: x*y, factoList)

print("factorial for number {0} is {1}" .format(num, output))
