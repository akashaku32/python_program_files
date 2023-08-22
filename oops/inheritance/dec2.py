def dec_fun(fn):
    def inner_fun(n1,n2):
        n1=n1**2
        n2=n2**2
        return fn(n1,n2)
    return inner_fun
@dec_fun
def add(n1,n2):
    return n1+n2
@dec_fun
def prod(n1,n2):
    return n1*n2

print(add(1,2))
print(prod(2,3))

