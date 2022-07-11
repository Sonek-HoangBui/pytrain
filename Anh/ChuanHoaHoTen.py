
def Nhaphoten():
    return input("Moi ban nhap ho ten: ")   

def stringtolist(ten : str):    #  " Vu    HoANg    anH  "
    list_ten = ten.split(" ")
    listhoten = []  
    for i in list_ten:
        if i != "":
            listhoten.append(i.casefold().capitalize())
    return listhoten

def chuanhoa(listhoten:list):
    hoten_str = " "
    for i in listhoten:
        hoten_str += i + " "
    hoten_str = hoten_str[:len(hoten_str)-1]
    print("Chuoi da chuan hoa :" +hoten_str)


ten = Nhaphoten()
listhoten = stringtolist(ten)
chuanhoa(listhoten)
      
    

        
     