#determine if the number is an amstrong number
num = input("Enter the number = ")

#helper function to calculate amstrong number 
def Amstrong_maff(number, length):
	return pow(number, length)

#turn single number in individual digits
numList = [int(num) for num in str(num)]
#print(*numList)

#Get Length of the digit
lenDigit = len(numList)
#print(lenDigit)

total = 0

#Calculate Amstrong number 
for i in numList:
	#calculte power of individual digits 
	power = Amstrong_maff(i, lenDigit)
#	print(power)
	#Addup all the power
	total = total + power
#	print(total)

#print(num)

#check if it is amstrong number
if int(total) == int(num):
	print("{0} is an Armstrong number".format(num))
else:
	print("{0} is not an Armstrong number".format(num))
