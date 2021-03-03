import re
txt = "Hey there Nikhil this side"
l = []
x = re.split(" ",txt)
for i in x:
	l.insert(0,i)
longString = max(l,key = len)
print("Longest String: ",longString)
print("Length of Longest String",len(longString))
