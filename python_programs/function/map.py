#MAP FUNCTION

lst=[1,2,3,4,5]
# cube=list(map(lambda l:l**3,lst))
# print(cube)
# square=list(map(lambda s:s**2,lst))
# print(square)

#FILTER FUNCTION

evens=list(filter(lambda n:n%2==0,lst))
print(evens)
num_gt3=list(filter(lambda n:n>3,lst))
print(num_gt3)
odd=list(filter(lambda n:n%2!=0,lst))
print(odd)