for i in range(1,6):
    for j in range(6,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    for j in range(i+1,12):
        print(" ",end="")
    for j in range(15,8+i,-1):
        print(" ",end="")
    for j in range(i):
        print("* ",end="")
    print()
    
for i in range(6,11):
    for j in range(1,6):
        print("  ",end="")
    for j in range(i-6):
        print(" ",end="")
    for j in range(11,i,-1):
        print("* ",end="")
    print()

