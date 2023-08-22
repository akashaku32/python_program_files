student={"roll":1234,"name":"anil","age":19,"course":"bca"}
# print(student.values())
# #return all values in dictionary
# print(student.keys())
# #return all keys in dictionary
# print(student.items())
# for k,v in student.items():
#     print(k,v)
# print(student.get("roll")) #if invalid key return none
student.pop("age")
print(student)
