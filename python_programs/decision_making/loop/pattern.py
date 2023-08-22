num=4
for i in range(num+1):
    for j in range(i):
        print(num,end="")
    print()
num=4
d=0
for i in range(num):
    d=d+((10**i)*num)
    print(d)
for i in range(1,num+1):
    print(i*str(num))