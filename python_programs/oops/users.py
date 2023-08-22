class users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},
    ]
    def get(self):
        return self.data
    def retrieve(self,id):
       return [i for i in self.data if i.get("id")==id]
    def post(self,dat):
        self.data.append(dat)
    def destroy(self,id):
        k=[i for i in self.data if i.get("id")==id][0]
        self.data.remove(k)
    def put(self,id,dat):
        k=[i for i in self.data if i.get("id")==id][0]
        pos=self.data.index(k)
        self.data[pos]=dat

                
        


obj=users()
print(obj.retrieve(1))
student_data={"id":7,"name":"sujith","email":"sujith@gmail.com","password":"4345435"}
obj.post(student_data)
obj.destroy(6)
stud_data={"id":5,"name":"suji","email":"suji@gmail.com","password":"434545"}
obj.put(5,stud_data)
print(obj.get())


#list->get
#read->retrieve
#create->post
#update->put
#delete->destroy
#
