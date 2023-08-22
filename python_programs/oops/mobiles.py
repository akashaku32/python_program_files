class mobiles:
    data=[
        {"id":100,"name":"redminote12","price":23000,"network":"5g"},
        {"id":101,"name":"pixel7pro","price":73000,"network":"5g"},
        {"id":102,"name":"s23 ultra","price":123000,"network":"5g"},
        {"id":103,"name":"iphone 13 pro","price":143000,"network":"5g"},
        {"id":104,"name":"oneplusnord2","price":20000,"network":"5g"},
        {"id":105,"name":"realme note 9","price":25000,"network":"5g"},
        {"id":106,"name":"poco gt","price":29000,"network":"5g"}
        ]
    def get(self):
        return self.data
    def retrieve(self,id):
        v=[i for i in self.data if i.get("id")==id]
        return v
    def post(self,value):
        self.data.append(value)
    def put(self,id,value):
        v=[i for i in self.data if i.get("id")==id][0]
        pos=self.data.index(v)
        self.data[pos]=value
    def destroy(self,id):
        v=[i for i in self.data if i.get("id")==id][0]
        self.data.remove(v)
    

obj1=mobiles()

print(obj1.retrieve(101))
mob_value={"id":107,"name":"poco x3","price":20000,"network":"5g"}
obj1.post(mob_value)
mobile_value={"id":105,"name":"poco","price":21000,"network":"5g"}
obj1.put(105,mobile_value)
obj1.destroy(105)
print(obj1.get())






