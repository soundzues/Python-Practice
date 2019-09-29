#find the larges number in array
#initialize arr:
arr = []

#take number of input from user
num = int(input("please enter the number of elements you want to enter: ")) #range

#take inputs from the user
for i in range(num):
	x = int(input())
	arr.append(x)

#easy way
#print("largest number in the array is {0}".format(max(arr)))

#mannual:

#start at 0th element
maxim = arr[0]
for i in range(num):
	#print(i)
	if arr[i] > maxim:
		maxim = arr[i]


print("largest number in the array is {0}".format(maxim))
