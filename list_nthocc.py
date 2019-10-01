#Program to remove Nth occurance of given word
import sys

#intialize list 
mylist = []

#take number of input from user
num = int(input("please enter the number of elements you want to enter: ")) #range

#take inputs from the user
for i in range(num):
	x = input()
	mylist.append(x)

print(*mylist)

#store the element you want to delete
element = input("enter the element you want to delete: ")

#store the occurance you want to delete
n = int(input("enter the ouccarance you want to delete: "))

#look for all the occurances
index = [i for i, x in enumerate(mylist) if x == element]


#error check on occurance
if(n > len(index) or len(index) == 0):
	print("ERROR: YOU ARE TRYING TO GET RID IF OCCURANCE THAT DOES NOT EXIST IN THE LIST OR ELEMENT DOES NOT EXISIT IN THE LIST")	
	sys.exit(1)

#deleting the following index 
del mylist[index[n-1]]

print(*mylist)
