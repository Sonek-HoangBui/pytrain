# from logging import _Level
# from pkg_resources import working_set


from distutils.ccompiler import gen_lib_options
from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class CanBo:
    _name: str
    _age: int
    _gender: Gender
    _addr: str

    def __init__(self, name, age, gender, addr):
        self._name = name
        self._age = age
        self._gender = gender 
        self._addr = addr
        
    def inputInfo(self):
        self._name = str(input("Input name: "))
        self._age = int(input("Input age: "))
        self._gender = str(input("Inputgender: "))
        if self._gender == Gender.FEMALE:
            print("Gender: ", self.gender)
        elif self.gender == Gender.MALE:
            print("Gender: ", self.gender)
        else:
            print("Gender: Khác")
            
        self.addr = str(input("Input addr: "))
        
    def showInfo(self):
        print("name: ", self._name)
        print("age: ", self._age)
        print("gender: ", self._gender)
        print("addr: ", self._addr)
        

class CongNhan(CanBo):
    #__Level = ''
    def __init__(self, name, age, gender, addr, level):
        super().__init__(name, age, gender, addr)
        self.level = level
        
    def inputInfo(self):
        super().inputInfo()
        self.level = int(input("Input level: "))
        if self.level >= 1 and self.level <= 10:
            print(self.level)
        else:
            print("Cấp bậc chỉ từ 1 đến 10")
            self.level = int(input("Input level: "))
        
    def showInfo(self):
        super().showInfo()
        print("level: ", self.level)
        
        
class KySu(CanBo):
    #__Nganh  = ''
    def __init__(self, name, age, gender, addr, NganhDaoTao):
        super().__init__(name, age, gender, addr)
        self.NganhDaoTao = NganhDaoTao
    # def setNganh(self):
    #     return 0
    def inputInfo(self):
        super().inputInfo()
        self.NganhDaoTao = input("Input NganhDaoTao: ")
        
    def showInfo(self):
        super().showInfo()
        print("NganhDaoTao: ", self.NganhDaoTao)
        
        
class NhanVien(CanBo):
    #__Task = ''
    def __init__(self, name, age, gender, addr, Task):
        super().__init__(name, age, gender, addr)
        self.Task = Task
    # def setTask(self):
    #     return 0
    
    def inputInfo(self):
        super().inputInfo()
        self.Task = input("Input Task: ")
        
    def showInfo(self):
        super().showInfo()
        print("Task: ", self.Task)
       
CongNhan = CongNhan("Lan", 18, "Nu", "Ha Noi", "4")
CongNhan.inputInfo()
CongNhan.showInfo()
                    
        
# NhanVien = NhanVien("Lan", 18, "Nu", "Ha Noi", "BA")
# NhanVien.inputInfo()
# NhanVien.showInfo()
                
            
    
    
    
    
# Một đơn vị sản xuất gồm có các cán bộ là công nhân, kỹ sư, nhân viên. Mỗi cán bộ cần quản lý các dữ
# liệu: Họ tên, tuổi, giới tính(name, nữ, khác), địa chỉ.

# Cấp công nhân sẽ có thêm các thuộc tính riêng: Bậc (1 đến 10).
# Cấp kỹ sư có thuộc tính riêng: Nghành đào tạo.
# Các nhân viên có thuộc tính riêng: công việc.

# Yêu cầu 1: Xây dựng các lớp CongNhan, KySu, NhanVien kế thừa từ lớp CanBo.

# Yêu cầu 2: Xây dựng lớp QLCB(quản lý cán bộ) cài đặt các phương thức thực hiện các chức năng sau:

# Thêm mới cán bộ.
# Tìm kiếm theo họ tên.
# Hiện thị thông tin về danh sách các cán bộ.
# Thoát khỏi chương trình.