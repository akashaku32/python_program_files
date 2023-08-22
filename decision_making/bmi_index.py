weight=60 #in kilograms
height=2.3 #in meters
bmi=weight/(height**2)
if(bmi<18.5):
    print("underweight")
elif(bmi<=24.9):
    print("normal weight")
elif(bmi<=29.9):
    print("overweight")
elif(bmi<=34.9):
    print("obesity class 1")
elif(bmi<=39.9):
    print("obesity class 2")
else:
    print("obesity class 3")