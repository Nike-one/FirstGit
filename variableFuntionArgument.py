def fun(a,*b,**c): #b = tuple #c = dictionary
    print("a=",a)
    print(b)
    print(c)
    return

fun(1,2,3,n=10,p=9)

#Output
#a= 1
#(2, 3)
#{'n': 10, 'p': 9}
