
def div_upgrade(func):
    def inner(a,b):
        if a > b:
            return func(a,b)
        else:
            return func(b,a)
    return inner

@div_upgrade
def div(x,y):
    return x/y

print(div(2,4))
