def max_three(num1,num2,num3):
    # if(num1>num2 and num1>num3):
    #     return num1
    # elif(num2>num1 and num2>num3):
    #     return num2
    # else:
    #     return num3
    return num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
print(max_three(10,30,20))