#factorial
num = int(input("Enter number: "))
f = 1
if num < 0:
	print("Enter postive number")
else:
	for i in range(2,num+1):
		f *= i 
print(f)