ch = str(input("Enter a String: "))

rev = ""
for i in range(len(ch)-1,-1,-1):
	rev += ch[i]

print(rev)