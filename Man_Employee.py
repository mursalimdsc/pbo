class Man_Employee:
    suku = "Bugis"
    empCount = 0
  
    def __init__(self,name,age, agama, jnskel, alamat, status,salary):
        self.name   = name
        self.salary = salary
        self.name   = name
        self.age    = age
        self.jnskel = jnskel
        self.agama  = agama
        self.alamat = alamat
        self.status = status
        Man_Employee.empCount +=1
   
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print ("Name :",self.name, ", Salary: ", self.salary)

    def biodata(self):
        #return f"{self.name} is {self.age} years old"
        return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat:{self.alamat} \nStatus: {self.status}"
    
tes_qois = Man_Employee("Mursalim",22,"Agama","Laki-laki","Batang","Jomblo",1000000)
print(tes_qois.biodata())
print("Suku: ", tes_qois.suku)

tes_qois.displayEmployee()
tes_qois.displayEmployee()
print ("total Employee %d" % Man_Employee.empCount)




