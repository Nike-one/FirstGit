#palindrome --> number remain same when read from either forward or backward e.g. 121 
n = int(input("Enter Number: "))
if n == n[::-1]:
	print("palindrome Number")
else:
	print("Not palindrome Number")

#Output Enter Number: 121 --> palidrome Number
