num=int(input())
for i in range(num):
    for j in range(i):
        print(" ",end="")
    for k in range(num,i,-1):
        if(k==num or k==i+1):
            print("* ",end="")
        elif(i==0):
            print("* ",end="")
        else:
            print("  ",end="")
    print()