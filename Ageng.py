class Manusia:
    # Class attribute
    suku = "Bugis"

    def __init__(self, name, age, agama, jnskel, alamat, status):
        self.name   = name
        self.age    = age
        self.jnskel = jnskel
        self.agama  = agama
        self.alamat = alamat
        self.status = status
    
    def biodata(self):
        #return f"{self.name} is {self.age} years old"
        return f"Nama: {self.name} \nUsia: {self.age} \nAgama: {self.agama} \nJenis Kelamin: {self.jnskel} \nAlamat:{self.alamat} \nStatus: {self.status}"
    
tes_ageng = Ageng("Ageng",22,"Agama","Laki-laki","Batang","Jomblo")
print(tes_ageng.biodata())
print("Suku: ", tes_ageng.suku)