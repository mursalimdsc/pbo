class Matematika:

    def __init__(self,nilai1,nilai2,nilai3,nilai4) -> None:
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3
        self.nilai4 = nilai4
        
        hasil = 0
    def penjumlahan(self):
        hasil =  self.nilai1+self.nilai2
        print (hasil)
        return hasil
    
    def perkalian(self):
        hasil = self.nilai1*self.nilai2*self.nilai3
        print(hasil)
        return hasil
    
    def pengurangan(self):
        hasil = self.nilai1-self.nilai2
        print (hasil)
        return hasil
    
    def perpangkatan(self):
        hasil = self.nilai1**self.nilai2
        print (hasil)
        return hasil
        

matematika = Matematika(100,10,20,20);
matematika.pengurangan()
matematika.penjumlahan()
matematika.perkalian()
matematika.perpangkatan()

