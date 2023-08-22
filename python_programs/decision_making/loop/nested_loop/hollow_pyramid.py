for i in range(8):
    for j in range(8,i,-1):
        
            print(" ",end="")
    for j in range(i):
        if(j==0 or j==i-1):
                print("* ",end="")
        elif(i==7):
              print("* ",end="")
        else:
              print("  ",end="")
        
    

    print()