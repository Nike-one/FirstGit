def fib(n):
    if n <=1:
        return n
        
    else:
        return fib(n-1) + fib(n-2)
        
n1 = int(input("enter number: "))

for i in range(0,n1):
    print(fib(i))

#output enter number: n1 = 5 --> 0 1 1 2 3
