def Factorial(num):
	fact = 1
	for i in range(1,num+1):
		fact=fact*i
	return fact
def AddNum(num):
	add = 0
	while(num!=0):
		add = add+Factorial(num%10)
		num//10
	return add
num = 145
if num==AddNum(num):
	print('special number')
else:
	print('not special number')
