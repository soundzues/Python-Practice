#sum array 
from functools import reduce

#initialize arr:
arr = []

#take number of input from user
num = int(input("please enter the number of elements you want to enter: ")) #range

#take inputs from the user
for i in range(num):
	x = int(input())
	arr.append(x)

#test print all var
i#print(*arr)

#sum all array elements:
total = reduce(lambda x,y: x+y, arr)

print(total)
