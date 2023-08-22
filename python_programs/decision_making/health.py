tummy_size=50
buttock_size=20
gender="Male"
calc=tummy_size/buttock_size
if(gender=="Male"):
    if(calc<=.80):
        print("Health Risk=low and body shape=Pear")
    elif(calc<=.85):
        print("Health Risk=Moderate and body shape=Avocado")
    elif(calc>.85):
        print("Health Risk=High and body shape=Apple")
else:
    if(calc<=.95):
        print("Health Risk=low and body shape=Pear")
    elif(calc<=1):
        print("Health Risk=Moderate and body shape=Avocado")
    elif(calc>1):
        print("Health Risk=High and body shape=Apple")

