#Prgoram to interchange first and last elements
#initialize arr:
mylist = []

#take number of input from user
num = int(input("please enter the number of elements you want to enter: ")) #range

#take inputs from the user
for i in range(num):
x = int(input())
mylist.append(x)
 
#print out orignal list
print(*mylist)
 
#get length of the list
size = len(mylist)
 
#Interchanging:  
temp = mylist[0] 
mylist[0] = [size - 1] 
mylList[size - 1] = temp 
    
#printin out
print(*mylist)
