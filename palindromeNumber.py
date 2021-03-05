#palindrome --> number remain same when read from either forward or backward e.g. 121 
n = int(input("Enter Number: "))
temp = n
rev = 0
while n>0:
	r = n%10
	rev = rev*10 + r 
	n = n//10


if (temp == rev):
	print("palidrome")
else:
	print("Not palidrome")

#Output Enter Number: 121 --> palidrome
