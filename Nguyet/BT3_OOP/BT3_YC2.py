
# from audioop import add
# from xmlrpc.server import list_public_methods
import BT3_CanBo
from Nguyet.BT3_OOP.BT3 import CanBo
  
class QuanLyCB:
    
    listCanBo = []
    
    def VolCB(self, listCanBo):
        listCanBo = self.listCanBo
        return listCanBo.__len__()
    
    def AddCB(self):
        name = input("Nhap ten can bo: ")
        age = input("Nhap tuoi can bo: ")
        gender = input("Nhap gioi tinh can bo: ")
        addr = input("Nhap dia chi can bo: ")
        cb = CanBo(name, age, gender, addr)
        self.listCanBo.append(cb)
        

    def FindName(self, key):
        listCB = []
        if (self.VolCB() > 0):
            for cb in self.listCanBo:
                if (key.upper() in cb._name.upper()):
                    listCB.append(cb)
        return listCB
            
    def showCB(self, listCB):
        print (self.name, self.age, self.gender, self.addr)
        
         
#QuanLyCB.VolCB()
QuanLyCB.AddCB()
      
    
# class CanBo:
#     def add(self, name, age, gender, addr):
#         #global listCanBo
#         while True: 
#             print(Nhập tên: )
    
#     def search(self, name):
#         print("Tim kiem theo ho ten")
        
#     def show(self):
#         print("name: ", self.name + "age: ", self.age + "gender: ", self.gender + "addr: ", self.addr + "level: ", self.level)
        