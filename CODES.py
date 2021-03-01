
#area of triangle

a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triange: ", area)

# program to convert hieght into cm

f=float(input("enter foot hieght: "))
inch = float(input("enter inch: "))
t = (f*12)+inch
cm = inch*2.5
print("hieght: ", cm, "cm")


#covert time into second

d = int(input("days: "))
h = int(input("hours: "))
m = int(input("minutes: "))
s = int(input("seconds: "))
s += (d*24*60*60)+(h*60*60)+(m*60)
print("total sec = ", s)

# Distance between two points

x1 = int(input("enter x1: "))

x2 = int(input("enter x2: "))

y1 = int(input("enter y1: "))

y2 = int(input("enter y2: "))


distance = (  (x2-x1)**2 + (y2-y1)**2 )**0.5


print("Distance: ", distance)
