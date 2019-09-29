#rotate an array:
import sys

#Initialize arr:
arr = []
temp1 = []
temp2 = []

#take number of input from user
num = int(input("please enter the number of elements you want to enter: ")) #range

#take inputs from the user
for i in range(num):
	x = int(input())
	arr.append(x)

print(*arr)

#easy way
#arr.reverse()
#print(*arr)

#manual

#get the length of the array
length = len(arr)

#get the elements you want to reverse
#make sure the elements to be reversed are in the length of the array
elements = (int(input("enter the elements you want to reverse: ")))

if(elements > length):
	print("ERROR: length of the elements to be reversed is greater than length of array")
	sys.exit(1)

#function to rotate elements
def rotate(a, n, d):
	reverse_arr = []
	#print(a[0:d:1])
	temp1 = a[0:d:1] #store the elements you want to put back
	#print(*temp1)

	temp2 = a[d:n:1] #store the elements you want to put front
	#print(*temp2)

	reverse_arr = temp2 + temp1 
	print(*reverse_arr)
	
	

rotate(arr, length, elements)

#print(len(arr));



